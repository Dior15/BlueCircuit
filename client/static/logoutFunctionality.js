document.addEventListener('DOMContentLoaded', () => {
    fetch('/check_login')
      .then(response => response.json())
      .then(data => {
        const userSection = document.getElementById('user-section');
        if (data.logged_in) {
          userSection.innerHTML = `
            <div class="dropdown">
            <a id="welcomeButton"><button> &#x25BC Welcome, ${data.user}! &#x25BC</button></a>
              <div class="dropdown-content">
                <a href="/watchlist" id="watchlist">Your watchlist</a>
                <a href="/logout" id="logout-link">Logout</a>
              </div>
            </div>
          `;
          document.getElementById("signin-or-up").innerHTML=""; // Removing the sign in and sign up buttons from the bottom of the page when the user is logged in
          
          // Adding an event listener to the watchlist link to redirect to the watchlist page
          document.getElementById('watchlist').addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = '/watchlist'; // Redirect to watchlist.html
          });
          
          // event listener to log tthe user out
          document.getElementById('logout-link').addEventListener('click', (e) => {
            e.preventDefault();
            fetch('/logout', { method: 'POST' })
              .then(() => location.reload());
          });
        }
      });
  });