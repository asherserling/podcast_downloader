from podcast_download.f_interface import app, FlaskPodcasts

destination_dir = './downloads'
flask_podcast_app = FlaskPodcasts(app, destination_dir)


if __name__ == '__main__':
    flask_podcast_app.run()
