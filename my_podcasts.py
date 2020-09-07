import csv


class MyPodcasts:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.my_podcasts = self.load_my_podcasts()
        self.episode_menus = {}

    def load_my_podcasts(self):
        podcasts = {}
        with open(self.csv_file, 'r') as infile:
            infile.readline()  # skip first line
            reader = csv.reader(infile)
            for row in reader:
                podcasts[row[0]] = row[1]
            return podcasts

    def dump_my_podcasts(self):
        with open(self.csv_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['podcast title', 'url'])
            writer.writerows(self.my_podcasts.items())

    def add(self, title, url):
        self.my_podcasts[title] = url
        self.dump_my_podcasts()

    def remove(self, title):
        del self.my_podcasts[title]
        self.dump_my_podcasts()

    def get_url_for(self, title):
        return self.my_podcasts[title]

    def get_podcasts(self):
        return self.my_podcasts


csv_file = 'C:\\Users\\Asher\\Desktop\\podcast_download\\data\\podcasts.csv'
my_podcasts = MyPodcasts(csv_file)
