import csv
import pickle


class MyPodcasts:
    def __init__(self, data_file):
        self.podcast_loader = podcast_loader_factory(self, data_file)
        self.my_podcasts = self.load_podcasts()
        self.episode_menus = {}

    def load_podcasts(self):
        return self.podcast_loader.load_podcasts()

    def dump_podcasts(self):
        return self.podcast_loader.dump_podcasts()

    def add(self, title, url):
        self.my_podcasts[title] = url
        self.dump_podcasts()

    def remove(self, title):
        del self.my_podcasts[title]
        self.dump_podcasts()

    def get_url_for(self, title):
        return self.my_podcasts[title]

    def get_podcasts(self):
        return self.my_podcasts


def podcast_loader_factory(parent, data_file):
    if data_file.endswith('.csv'):
        return PodcastsFromCsv(parent, data_file)
    elif data_file.endswith('.pkl'):
        return PodcastsFromPickle(parent, data_file)


class PodcastsFromCsv:
    def __init__(self, parent, csv_file):
        self.parent = parent
        self.csv_file = csv_file

    def load_podcasts(self):
        podcasts = {}
        with open(self.csv_file, 'r') as infile:
            infile.readline()  # skip first line
            reader = csv.reader(infile)
            for row in reader:
                podcasts[row[0]] = row[1]
        return podcasts

    def dump_podcasts(self):
        podcasts = self.get_podcasts()
        with open(self.csv_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['podcast title', 'url'])
            writer.writerows(podcasts.items())

    def get_podcasts(self):
        return self.parent.get_podcasts()


class PodcastsFromPickle:
    def __init__(self, parent, pickle_file):
        self.parent = parent
        self.pickle_file = pickle_file

    def load_podcasts(self):
        with open(self.pickle_file, 'rb') as infile:
            podcasts = pickle.load(infile)
        return podcasts

    def dump_podcasts(self):
        podcasts = self.get_podcasts()
        with open(self.pickle_file, 'wb') as outfile:
            pickle.dump(podcasts, outfile, pickle.HIGHEST_PROTOCOL)

    def get_podcasts(self):
        return self.parent.get_podcasts()


if __name__ == '__main__':
    pass
