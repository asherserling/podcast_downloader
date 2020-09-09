from flask import render_template, request, url_for, redirect
from podcast_download.f_interface import app
from podcast_download.podcast import EpisodeMenu
from podcast_download.podcast import my_podcasts


@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


@app.route('/')
def index():
    return render_template('index.html',
                           podcasts=my_podcasts.get_podcasts())


@app.route('/podcast/<podcast_title>')
def podcast_page(podcast_title):
    episode_menu = my_podcasts.episode_menus.get(podcast_title)
    if not episode_menu:
        url = my_podcasts.get_url_for(podcast_title)
        interface = app.config['interface']
        episode_menu = my_podcasts.episode_menus[podcast_title] = EpisodeMenu(url, interface)
    return render_template('podcast_page.html',
                           episode_menu=episode_menu,
                           podcast_title=podcast_title)


@app.route('/download', methods=['POST'])
def download_episode():
    podcast_title = request.form['podcast_title']
    episode_id = int(request.form['episode_id'])
    episode_menu = my_podcasts.episode_menus[podcast_title]
    episode_menu.download_by_id(episode_id)
    return ""


@app.route('/settings')
def settings():
    return render_template('settings.html',
                           podcasts=my_podcasts.get_podcasts())


@app.route('/add', methods=['POST'])
def add_podcast():
    title = request.form['podcast_title']
    url = request.form['podcast_url']
    my_podcasts.add(title, url)
    return redirect(url_for('settings'))


@app.route('/remove/<podcast_title>')
def remove_podcast(podcast_title):
    actual_title = podcast_title.replace('%20', ' ')
    my_podcasts.remove(actual_title)
    return redirect(url_for('settings'))
