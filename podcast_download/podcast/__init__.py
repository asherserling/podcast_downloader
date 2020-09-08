import pathlib
import os

from .my_podcasts import MyPodcasts
from .episode_menu import EpisodeMenu

basedir = pathlib.Path(__file__).parent.absolute()

pkl_relative_path = 'data\\podcasts.pkl'
pkl_absolute_path = os.path.join(basedir, pkl_relative_path)

csv_relative_path = 'data\\podcasts.csv'
csv_absolute_path = os.path.join(basedir, csv_relative_path)

my_podcasts = MyPodcasts(pkl_absolute_path)
