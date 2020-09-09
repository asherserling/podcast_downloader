import podcast_download.cli.app as cli_app


app = cli_app.PodcastApp(destination_dir='./downloads')
app.run()
