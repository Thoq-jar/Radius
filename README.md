# Radius

A simple Python web framework.
This was more for fun than to be used but feel free to,
just dont use Radial (the server) to host a production deployment!

## Layout
The `radius/` directory is where the library lives.
Your app lives in the `app/` directory in the `index.py` file.
The utility scripts to assit you live in the `utility/` directory.

## Running
**Linux/macOS**
```bash
chmod +x utility/run_cli
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
./utility/run_cli
```

**Windows**
```bash
pip install -r requirements.txt
python utility\run_cli
```

## License
This project uses the [MIT](https://opensource.org/license/mit) license, see the [LICENSE](LICENSE.md) for more details
