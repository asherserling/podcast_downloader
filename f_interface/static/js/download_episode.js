var download_episode = function (podcast_title, episode_id) {
    var podcast = {
        podcast_title: podcast_title,
        episode_id: episode_id
    }
    $.post('/download', podcast)
}

var podcast_title = document.querySelector('.secret-title').getAttribute('id')
var episode_links = document.querySelector('.episode-links').children

var i, n = episode_links.length
for (i = 0; i < n; i++) {
    var episode_link = episode_links[i]
    episode_link.addEventListener('click', download_episode.bind(null, podcast_title, i.toString()))
}
