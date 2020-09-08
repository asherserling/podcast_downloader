import webbrowser
import sys
from threading import Timer

from podcast_download.f_interface import app as flask_app
from podcast_download.cli.app import PodcastApp


def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')


def run_flask_interface():
    Timer(2, open_browser).start()
    flask_app.run(port=2000)


def run_cl_interface():
    cli_app = PodcastApp()
    cli_app.run()


if __name__ == '__main__':
    if sys.argv[-1] == 'flask':
        run_flask_interface()
    else:
        run_cl_interface()
