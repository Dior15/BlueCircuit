document.addEventListener('DOMContentLoaded', () => {
    fetch('/check_login')
      .then(response => response.json())
      .then(data => {
        const userSection = document.getElementById('user-section');
        if (data.logged_in) {
          userSection.innerHTML = `
            <div class="dropdown">
              <button class="is-flex">Welcome, ${data.user}!</button>
              <div class="dropdown-content">
                <a href="/profile">${data.user}'s watchlist</a>
                <a href="/logout" id="logout-link">Logout</a>
              </div>
            </div>
          `;
          // event listener to log tthe user out
          document.getElementById('logout-link').addEventListener('click', (e) => {
            e.preventDefault();
            fetch('/logout', { method: 'POST' })
              .then(() => location.reload());
          });
        }
      });
  });