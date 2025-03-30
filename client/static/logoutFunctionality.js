document.addEventListener('DOMContentLoaded', () => {
    fetch('/check_login')
      .then(response => response.json())
      .then(data => {
        const userSection = document.getElementById('user-section');
        if (data.logged_in) {
          userSection.innerHTML = `
            <div class="dropdown">
            <a id="welcomeButton"><button>👁 Welcome, ${data.user}!!</button></a>
              <div class="dropdown-content">
                <a href="/watchList" id="watchlist">Your watchlist</a>
                <a href="/logout" id="logout-link">Logout</a>
              </div>
            </div>
          `;
          document.getElementById("signin-or-up").innerHTML=""; // Removing the sign in and sign up buttons from the bottom of the page when the user is logged in
          // event listener to log tthe user out
          document.getElementById('logout-link').addEventListener('click', (e) => {
            e.preventDefault();
            fetch('/logout', { method: 'POST' })
              .then(() => location.reload());
          });
        }
      });
  });