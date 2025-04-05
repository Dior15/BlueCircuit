document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('watchlist-toggle-btn');

  if (!button) return;

  let isSaved = button.getAttribute('data-saved') === 'true';
  const movieId = button.getAttribute('data-movie-id');

  button.addEventListener('click', () => {
    const endpoint = isSaved ? '/watchlist/remove' : '/watchlist/add';

    fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ movie_id: movieId })
    })
      .then(res => res.json())
      .then(data => {
        alert(data.message);

        if (data.success) {
          // Toggle state
          isSaved = !isSaved;
          button.setAttribute('data-saved', isSaved);

          // Update button text and style
          if (isSaved) {
            button.innerHTML = "&#45; Remove from Watchlist";
            button.style.backgroundColor = "#1c1c1c";
          } else {
            button.innerHTML = "&#43; Add to Watchlist";
            button.style.backgroundColor = "#1c1c1c";
          }
        }
      })
      .catch(err => {
        console.error("Toggle failed:", err);
        alert("Something went wrong. Please try again.");
      });
  });
});
