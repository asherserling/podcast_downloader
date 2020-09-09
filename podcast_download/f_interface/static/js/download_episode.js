var download_episode = function (podcast_title, episode_id) {
    var podcast = {
        podcast_title: podcast_title,
        episode_id: episode_id
    }
    var status_element = ".status-" + episode_id;
    $.post('/download', podcast, function () {
        insert_html(status_element, "Download complete")
    })
    insert_html(status_element, "Downloading....")
}

var insert_html = function (selector, text) {
    var element = document.querySelector(selector);
    element.innerText = text;
}

var podcast_title = document.querySelector('.secret-title').getAttribute('id');
var episode_links = document.querySelectorAll('.episode');

var i, n = episode_links.length;
for (i = 0; i < n; i++) {
    var episode_link = episode_links[i];
    var episode_id = episode_link.getAttribute('id');
    episode_link.addEventListener('click', download_episode.bind(null, podcast_title, episode_id))
}
