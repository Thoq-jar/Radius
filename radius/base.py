from http.server import HTTPServer, BaseHTTPRequestHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import socket
import importlib
import sys
import os
from pathlib import Path
import threading
import websockets
import asyncio
import json

ws_clients = set()

banner = """
██████╗  █████╗ ██████╗ ██╗██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║██║   ██║██╔════╝
██████╔╝███████║██║  ██║██║██║   ██║███████╗
██╔══██╗██╔══██║██║  ██║██║██║   ██║╚════██║
██║  ██║██║  ██║██████╔╝██║╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚══════╝
"""

async def websocket_handler(websocket):
    try:
        ws_clients.add(websocket)
        await websocket.wait_closed()
    finally:
        ws_clients.remove(websocket)

async def notify_clients():
    if ws_clients:
        message = json.dumps({"type": "reload"})
        await asyncio.gather(*[client.send(message) for client in ws_clients])

class RadiusHTTPServer(HTTPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        super().server_bind()

class RadiusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            app_path = str(Path(__file__).parent.parent / 'app')
            if app_path not in sys.path:
                sys.path.insert(0, app_path)

            if 'index' in sys.modules:
                index_module = importlib.reload(sys.modules['index'])
            else:
                index_module = importlib.import_module('index')

            content = index_module.main()

            websocket_script = """
            <script>
                (function() {
                    let ws_url = 'ws://' + window.location.hostname + ':31416';
                    let ws = new WebSocket(ws_url);

                    ws.onmessage = function(event) {
                        let data = JSON.parse(event.data);
                        if (data.type === 'reload') {
                            console.log('Reloading page...');
                            window.location.reload();
                        }
                    };

                    ws.onclose = function() {
                        console.log('WebSocket closed, attempting to reconnect...');
                        setTimeout(function() {
                            window.location.reload();
                        }, 1000);
                    };
                })();
            </script>
            """

            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>New Radius App</title>
                <script src="https://cdn.tailwindcss.com"></script>
                {websocket_script}
            </head>
            {content}
            </html>
            """

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode())

        except Exception as e:
            error_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Radius Error</title>
                <style>
                    body {{ font-size: 120%; font-family: sans-serif; padding: 2rem; background: black; color: white }}
                    .error {{ background: black; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(255,255,255,0.1); }}
                    pre {{ background: #111111; padding: 1rem; border-radius: 4px; overflow-x: auto; }}
                </style>
            </head>
            <body> <div class="error"> <h1>[500] Radial: Error ocured</h1> <pre>{str(e)}</pre> <code>Radial v1.0.0</code> </div> </body>
            </html>
            """
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(error_content.encode())

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if isinstance(event.src_path, str) and event.src_path.endswith(('.py', '.css')):
            print(f"Reloading: {event.src_path}...")
            asyncio.run(notify_clients())

class Radius:
    def __init__(self):
        self.httpd = None
        self.observer = None
        self.ws_server = None
        self.ws_loop = None

    async def start_websocket_server(self):
        self.ws_server = await websockets.serve(websocket_handler, '127.0.0.1', 31416)
        await self.ws_server.wait_closed()

    def run_websocket_server(self):
        self.ws_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.ws_loop)
        self.ws_loop.run_until_complete(self.start_websocket_server())
        self.ws_loop.run_forever()

    def run(self, server_class=RadiusHTTPServer, handler_class=RadiusHandler, lan=False):
        print(banner)
        port = 31415
        if lan:
            address = "0.0.0.0"
            print("Exposing Radial to lan could be a privacy risk, set `radius.serve(expose=False)` to disable!")
        else:
            address = "127.0.0.1"

        ws_thread = threading.Thread(target=self.run_websocket_server, daemon=True)
        ws_thread.start()

        server_address = (f'{address}', port)
        print(f"Radial listening on http://{address}:{port}")

        try:
            self.httpd = server_class(server_address, handler_class)
        except OSError:
            time.sleep(1)
            self.httpd = server_class(server_address, handler_class)

        event_handler = FileChangeHandler()
        self.observer = Observer()
        self.observer.schedule(event_handler, path='app', recursive=True)
        self.observer.start()

        try:
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            self.cleanup()

    def cleanup(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
        if self.httpd:
            self.httpd.server_close()
        if self.ws_server:
            self.ws_server.close()
        if self.ws_loop:
            self.ws_loop.stop()

    def serve(self, expose=False):
        try:
            self.run(lan=expose)
        except KeyboardInterrupt:
            print("\nRadial interrupted! Stopping now...")
            self.cleanup()
            if __name__ != "__main__":
                os.kill(os.getpid(), 9)
            exit(0)
        except Exception as e:
            print(f"Radial encountered an error: {e}")
            import traceback
            traceback.print_exc()
            exit(1)
