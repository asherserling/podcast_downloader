from flask import Flask


app = Flask(__name__)

from podcast_download.f_interface import routes
