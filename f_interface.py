import webbrowser

from podcast_download.f_interface import app


def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')


if __name__ == '__main__':
    open_browser()
    app.run(port=2000)
