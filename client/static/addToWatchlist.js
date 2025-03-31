document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('add-to-watchlist');
  
    if (button) {
      button.addEventListener('click', () => {
        // Grab the movie ID from the URL
        const pathParts = window.location.pathname.split('/');
        const movieId = pathParts[pathParts.length - 1];
  
        fetch('/watchlist/add', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ movie_id: movieId })
        })
        .then(res => res.json())
        .then(data => {
          alert(data.message); // Show feedback to the user
        })
        .catch(err => {
          console.error("Error adding to watchlist:", err);
          alert("Something went wrong. Please try again.");
        });
      });
    }
  });
  