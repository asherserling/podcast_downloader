from flask import Flask


app = Flask(__name__)

from podcast_download.f_interface import routes


# A wrapper for flask app to add get_destination_dir method
# required by EpisodeMenu class
class FlaskPodcasts:
    def __init__(self, flask_app, destination_dir):
        flask_app.config['interface'] = self
        self.flask_app = flask_app
        self.destination_dir = destination_dir

    def run(self):
        self.flask_app.run()

    def get_destination_dir(self):
        return self.destination_dir
