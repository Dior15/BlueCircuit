// Get the modals
var loginModal = document.getElementById("loginModal");
var accountCreateModal = document.getElementById("createAccountModal");

// Get the buttons that open the modals
var loginBtn = document.getElementById("signin-header");
var loginBtn2 = document.getElementById("loginButton2");
var createAccountBtn = document.getElementById("createAccountButton");

// Get the <span> elements that close the modals
var closeButtons = document.getElementsByClassName("close");

// When the user clicks the button, open the respective modal
loginBtn.onclick = function() {
  loginModal.style.display = "block";
}
loginBtn2.onclick = function() {
  loginModal.style.display = "block";
}
createAccountBtn.onclick = function() {
  accountCreateModal.style.display = "block";
}

// Close modals when clicking on the close button
for (let i = 0; i < closeButtons.length; i++) {
  closeButtons[i].onclick = function() {
    this.parentElement.parentElement.style.display = "none";
  }
}

// When the user clicks anywhere outside of a modal, close it
window.onclick = function(event) {
  if (event.target == loginModal) {
    loginModal.style.display = "none";
  }
  if (event.target == accountCreateModal) {
    accountCreateModal.style.display = "none";
  }
}