document.getElementById('add-to-watchlist').onclick = function() {
    // singnify on the front end that the user has added the movie to the watchlist
    document.getElementById('add-to-watchlist').innerHTML = "&#10004; Added!"
    document.getElementById('add-to-watchlist').style.backgroundColor = "#1c1c1c"
}