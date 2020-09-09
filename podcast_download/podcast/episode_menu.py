import requests
from xml.etree import ElementTree
import shutil
import os
from threading import Thread


class Episode:
    def __init__(self, url, title, parent):
        self.url = url
        self.title = title
        self.parent = parent
        self.id = None

    def download(self):
        download_thread = Thread(target=self._download)
        download_thread.start()

    def _download(self):
        resp = requests.get(self.url, stream=True)
        resp.decode_content = True

        destination_dir = self.parent.get_destination_dir()
        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)

        filename = _format_episode_title(self.title) + '.mp3'
        filename_with_directory = os.path.join(
            destination_dir,
            filename)

        print("Downloading and saving " + filename)

        with open(filename_with_directory, 'wb') as fout:
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
    def __init__(self, url, interface):
        self.interface = interface
        print(self.interface.get_destination_dir())
        self.url = url
        if url:
            self.episodes = self._load_episodes()

    def _load_episodes(self):
        resp = requests.get(self.url)
        tree = ElementTree.fromstring(resp.text)

        episodes = [
            Episode(
                url=item.find('enclosure').attrib['url'],
                title=item.find('title').text,
                parent=self
            )
            for item in tree.findall('channel/item')
        ]

        for i in range(len(episodes)):
            episodes[i].id = i
        return episodes

    def download_by_index(self, index):
        if not index or not (1 <= index <= len(self.episodes)):
            print('Invalid index')
            return
        episode = self.episodes[index - 1]
        episode.download()

    def download_all(self, indexes):
        for index in indexes:
            self.download_by_index(index)

    def _get_episode(self, id):
        for episode in self.episodes:
            if episode.id == id:
                return episode

    def download_by_id(self, id):
        episode = self._get_episode(id)
        episode.download()

    def get_destination_dir(self):
        return self.interface.get_destination_dir()

    def __repr__(self):
        return "<Episode Menu>"


if __name__ == "__main__":
    url = 'https://podcasts.files.bbci.co.uk/p02nq0gn.rss'
    episode_menu = EpisodeMenu(url)
    episode_menu.download_by_index(1)
