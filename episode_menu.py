import requests
from xml.etree import ElementTree
import shutil
import os


class Episode:
    def __init__(self, url, title):
        self.url = url
        self.title = title

    def download(self):
        resp = requests.get(self.url, stream=True)
        resp.decode_content = True

        base_file = _format_episode_title(self.title) + '.mp3'
        dest_file = os.path.join(
            'C:\\Users\\Asher\\Downloads\\podcasts',
            base_file)

        print("Downloading and saving " + base_file)

        with open(dest_file, 'wb') as fout:
            shutil.copyfileobj(resp.raw, fout)

    def __repr__(self):
        return f"<Episode {self.title}>"


def _format_episode_title(original_title):
    nonvalid = list('<>:"/\\|?*')
    formatted_title = "_".join(list(original_title.split()))
    for char in nonvalid:
        formatted_title = formatted_title.replace(char, '_')
    return formatted_title


class EpisodeMenu:
    def __init__(self, url=""):
        self.url = url
        if url:
            self.episodes = self._get_episodes()

    def _get_episodes(self):
        resp = requests.get(self.url)
        tree = ElementTree.fromstring(resp.text)

        return [
            Episode(
                item.find('enclosure').attrib['url'],
                item.find('title').text
            )
            for item in tree.findall('channel/item')
        ]

    def list_episodes(self, limit=0):
        if not limit:
            limit = len(self.episodes)

        if not self.url:
            print('Need a url to list episodes')
            return

        menu_format = "{:3d}  {}"
        indexed_menu = list(enumerate(self.episodes, 1))
        for episode in indexed_menu[:limit]:
            print(menu_format.format(episode[0], episode[1].title))

    def download_by_index(self, index):
        if not index or not (1 <= index <= len(self.episodes)):
            print('Invalid index')
            return
        episode = self.episodes[index - 1]
        episode.download()


if __name__ == "__main__":
    url = 'https://podcasts.files.bbci.co.uk/p02nq0gn.rss'
    episode_menu = EpisodeMenu(url)
    episode_menu.download_by_index(1)
