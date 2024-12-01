class Tags():
    @staticmethod
    def body(children, tailwind=None) -> str:
        return f"<body class=\"{tailwind}\">{children}</body>"

    @staticmethod
    def script(children) -> str:
        return f"<script>{children}</script>"
    @staticmethod
    def h1(children, tailwind=None) -> str:
        return f"<h1 class=\"{tailwind}\">{children}</h1>"

    @staticmethod
    def h2(children, tailwind=None) -> str:
        return f"<h2 class=\"{tailwind}\">{children}</h2>"

    @staticmethod
    def h3(children, tailwind=None) -> str:
        return f"<h3 class=\"{tailwind}\">{children}</h3>"

    @staticmethod
    def h4(children, tailwind=None) -> str:
        return f"<h4 class=\"{tailwind}\">{children}</h4>"

    @staticmethod
    def h5(children, tailwind=None) -> str:
        return f"<h5 class=\"{tailwind}\">{children}</h5>"

    @staticmethod
    def h6(children, tailwind=None) -> str:
        return f"<h6 class=\"{tailwind}\">{children}</h6>"

    @staticmethod
    def p(children, tailwind=None) -> str:
        return f"<p class=\"{tailwind}\">{children}</p>"

    @staticmethod
    def div(children, tailwind=None) -> str:
        return f"<div class=\"{tailwind}\">{children}</div>"

    @staticmethod
    def span(children, tailwind=None) -> str:
        return f"<span class=\"{tailwind}\">{children}</span>"

    @staticmethod
    def a(children, href, tailwind=None) -> str:
        return f"<a href='{href}' class=\"{tailwind}\">{children}</a>"

    @staticmethod
    def img(src, alt="", tailwind=None) -> str:
        return f"<img src='{src}' alt='{alt}' class=\"{tailwind}\" />"

    @staticmethod
    def ul(children="", id=None, tailwind=None) -> str:
        return f"<ul id='{id}' class=\"{tailwind}\">{children}</ul>"

    @staticmethod
    def ol(children, tailwind=None) -> str:
        return f"<ol class=\"{tailwind}\">{children}</ol>"

    @staticmethod
    def li(children, tailwind=None) -> str:
        return f"<li class=\"{tailwind}\">{children}</li>"

    @staticmethod
    def br(tailwind=None) -> str:
        return f"<br class=\"{tailwind}\" />"

    @staticmethod
    def table(children, tailwind=None) -> str:
        return f"<table class=\"{tailwind}\">{children}</table>"

    @staticmethod
    def tr(children, tailwind=None) -> str:
        return f"<tr class=\"{tailwind}\">{children}</tr>"

    @staticmethod
    def td(children, tailwind=None) -> str:
        return f"<td class=\"{tailwind}\">{children}</td>"

    @staticmethod
    def th(children, tailwind=None) -> str:
        return f"<th class=\"{tailwind}\">{children}</th>"

    @staticmethod
    def form(children, action="", method="post", tailwind=None) -> str:
        return f"<form action='{action}' method='{method}' class=\"{tailwind}\">{children}</form>"

    @staticmethod
    def input(type="text", name="", value="", onkeypress=None, id=None, placeholder="", tailwind=None) -> str:
        return f"<input type='{type}' name='{name}' id='{id}' onkeypress='{onkeypress}' placeholder='{placeholder}' value='{value}' class=\"{tailwind}\" />"

    @staticmethod
    def button(children, type="button", id=None, onclick=None, tailwind=None) -> str:
        return f"<button type='{type}' id='{id}' onclick='{onclick}' class=\"{tailwind}\">{children}</button>"

    @staticmethod
    def textarea(children="", name="", rows="4", cols="50", tailwind=None) -> str:
        return f"<textarea name='{name}' rows='{rows}' cols='{cols}' class=\"{tailwind}\">{children}</textarea>"

    @staticmethod
    def select(options, name="", tailwind=None) -> str:
        return f"<select name='{name}' class=\"{tailwind}\">{options}</select>"

    @staticmethod
    def option(children, value="", tailwind=None) -> str:
        return f"<option value='{value}' class=\"{tailwind}\">{children}</option>"

    @staticmethod
    def label(children, for_id="", tailwind=None) -> str:
        return f"<label for='{for_id}' class=\"{tailwind}\">{children}</label>"

    @staticmethod
    def header(children, tailwind=None) -> str:
        return f"<header class=\"{tailwind}\">{children}</header>"

    @staticmethod
    def footer(children, tailwind=None) -> str:
        return f"<footer class=\"{tailwind}\">{children}</footer>"

    @staticmethod
    def nav(children, tailwind=None) -> str:
        return f"<nav class=\"{tailwind}\">{children}</nav>"

    @staticmethod
    def main(children, tailwind=None) -> str:
        return f"<main class=\"{tailwind}\">{children}</main>"

    @staticmethod
    def section(children, tailwind=None) -> str:
        return f"<section class=\"{tailwind}\">{children}</section>"

    @staticmethod
    def article(children, tailwind=None) -> str:
        return f"<article class=\"{tailwind}\">{children}</article>"

    @staticmethod
    def aside(children, tailwind=None) -> str:
        return f"<aside class=\"{tailwind}\">{children}</aside>"

    @staticmethod
    def figure(children, tailwind=None) -> str:
        return f"<figure class=\"{tailwind}\">{children}</figure>"

    @staticmethod
    def figcaption(children, tailwind=None) -> str:
        return f"<figcaption class=\"{tailwind}\">{children}</figcaption>"

    @staticmethod
    def strong(children, tailwind=None) -> str:
        return f"<strong class=\"{tailwind}\">{children}</strong>"

    @staticmethod
    def em(children, tailwind=None) -> str:
        return f"<em class=\"{tailwind}\">{children}</em>"

    @staticmethod
    def small(children, tailwind=None) -> str:
        return f"<small class=\"{tailwind}\">{children}</small>"

    @staticmethod
    def code(children, tailwind=None) -> str:
        return f"<code class=\"{tailwind}\">{children}</code>"

    @staticmethod
    def pre(children, tailwind=None) -> str:
        return f"<pre class=\"{tailwind}\">{children}</pre>"

    @staticmethod
    def blockquote(children, tailwind=None) -> str:
        return f"<blockquote class=\"{tailwind}\">{children}</blockquote>"

    @staticmethod
    def cite(children, tailwind=None) -> str:
        return f"<cite class=\"{tailwind}\">{children}</cite>"

    @staticmethod
    def time(children, datetime="", tailwind=None) -> str:
        return f"<time datetime='{datetime}' class=\"{tailwind}\">{children}</time>"

    @staticmethod
    def mark(children, tailwind=None) -> str:
        return f"<mark class=\"{tailwind}\">{children}</mark>"

    @staticmethod
    def details(children, tailwind=None) -> str:
        return f"<details class=\"{tailwind}\">{children}</details>"

    @staticmethod
    def summary(children, tailwind=None) -> str:
        return f"<summary class=\"{tailwind}\">{children}</summary>"

    @staticmethod
    def dialog(children, tailwind=None) -> str:
        return f"<dialog class=\"{tailwind}\">{children}</dialog>"

    @staticmethod
    def canvas(children, width="", height="", tailwind=None) -> str:
        return f"<canvas width='{width}' height='{height}' class=\"{tailwind}\">{children}</canvas>"

    @staticmethod
    def audio(src, tailwind=None) -> str:
        return f"<audio src='{src}' class=\"{tailwind}\"></audio>"

    @staticmethod
    def video(src, tailwind=None) -> str:
        return f"<video src='{src}' class=\"{tailwind}\"></video>"

    @staticmethod
    def source(src, type="", tailwind=None) -> str:
        return f"<source src='{src}' type='{type}' class=\"{tailwind}\" />"

    @staticmethod
    def track(src, kind="", label="", tailwind=None) -> str:
        return f"<track src='{src}' kind='{kind}' label='{label}' class=\"{tailwind}\" />"

    @staticmethod
    def iframe(src, width="", height="", tailwind=None) -> str:
        return f"<iframe src='{src}' width='{width}' height='{height}' class=\"{tailwind}\"></iframe>"

    @staticmethod
    def progress(value="", max="", tailwind=None) -> str:
        return f"<progress value='{value}' max='{max}' class=\"{tailwind}\" />"

    @staticmethod
    def meter(value="", min="", max="", tailwind=None) -> str:
        return f"<meter value='{value}' min='{min}' max='{max}' class=\"{tailwind}\"></meter>"
