document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('remove-from-watchlist');
  
    if (button) {
      button.addEventListener('click', () => {
        // Grab the movie ID from the URL
        const pathParts = window.location.pathname.split('/');
        const movieId = pathParts[pathParts.length - 1];
  
        fetch('/watchlist/remove', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ movie_id: movieId })
        })
        .then(res => res.json())
        .then(data => {
          alert(data.message); // Show feedback to the user
          if (data.success) {
            // Update the button visually
            button.innerHTML = "&#10060; Removed!";
            button.style.backgroundColor = "#1c1c1c";
            button.disabled = true;
          }
        })
        .catch(err => {
          console.error("Error removing from watchlist:", err);
          alert("Something went wrong. Please try again.");
        });
      });
    }
  });
  