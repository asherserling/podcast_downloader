from episode_menu import EpisodeMenu
import config
from helpers import clear_screen
from time import sleep


class PodcastApp:
    def __init__(self):
        self.podcasts = config.podcasts
        self.episode_menu = None
        self.episode_menus = {}
        self.choose_podcast()

    def run(self):
        return self.choose_podcast()

    def choose_podcast(self):
        clear_screen()
        enumerated_podcasts = list(enumerate(self.podcasts, 1))

        indexed_podcasts = {
            str(index): title
            for index, title in enumerated_podcasts
        }

        menu_format = "{:2d}  {}"
        for index, title in enumerated_podcasts:
            print(menu_format.format(index, title))
        print()

        user_input = input('Enter the index of the podcast you want, or X to exit: ')

        if user_input.lower() == 'x':
            return

        elif not user_input.isnumeric():
            print('Input must be number')
            sleep(1)
            return self.choose_podcast()

        if not (1 <= int(user_input) <= len(self.podcasts)):
            print('Invalid index')
            sleep(1)
            return self.choose_podcast()

        podcast_title = indexed_podcasts[user_input]
        episode_menu = self.episode_menus.get(podcast_title)
   
        if not episode_menu:
            podcast_url = self.podcasts[podcast_title]
            episode_menu = EpisodeMenu(podcast_url)
            self.episode_menus[podcast_title] = episode_menu

        self.episode_menu = episode_menu
        self.choose_episode()

    def choose_episode(self):
        clear_screen()
        self.episode_menu.list_episodes(5)
        print()
        print('Exit: X, Back: B, See more episodes: S, Download by Index: Index')
        user_input = input().lower()

        if user_input == 'x':
            return
        if user_input == 'b':
            return self.choose_podcast()
        elif user_input == 's':
            return self.choose_menu_list_length()
        elif user_input.isdigit():
            self.episode_menu.download_by_index(int(user_input))
            return self.choose_episode()
        else:
            print('Invalid input')
            return self.choose_episode()

    def choose_menu_list_length(self):
        clear_screen()
        menu_length = input('Enter amount of podcasts to list, or A for all: ')

        if menu_length.lower() == 'a':  # EpisodeMenu.list_episodes will print all if 0 is given
            menu_length = 0

        elif not menu_length.isnumeric():
            print('Entry must be integer or A')
            return self.choose_menu_list_length()

        self.episode_menu.list_episodes(int(menu_length))

        print()
        print('Back: B, Download by Index: Index')
        user_input = input().lower()

        if user_input == 'b':
            return self.choose_podcast()
        elif user_input.isdigit():
            self.episode_menu.download_by_index(int(user_input))
            return self.choose_episode()
        else:
            print('Invalid input')
            return self.choose_menu_list_length()


if __name__ == '__main__':
    app = PodcastApp()
    app.run()
