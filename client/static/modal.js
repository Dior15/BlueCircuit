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

// Login form submission
document.getElementById("loginFormSubmit").onclick = function(event) {
  event.preventDefault(); // Prevent form submission

  const username = document.getElementById("loginUsernameField").value;
  const password = document.getElementById("loginPasswordField").value;

  // Fetch the CSV file
  fetch('/login', {
    method: 'POST', 
    headers: {
      'Content-Type': 'application/json', 
    }, 
    body: JSON.stringify({username, password}),
  })
  .then(response => response.json())
  .then(data => {
    
    //Display the message from the backend
    const messageElement = document.createElement("p");
    messageElement.style.textAlign = "center";

    if (data.success) {
      //Login successful
      messageElement.textContent = "Login successful!";
      messageElement.style.color = "green";


      //Redirect to homepage after successful login
      setTimeout(() => {
        window.location.href = "/";
      }, 1000); //Redirects user to the homepage after 1 second
    } 
    else if (data.success === false && data.message === "Username and password are required"){
      messageElement.textCaontent = "Username and password are required";
      messageElement.style.color = "red";
    }
    else if (data.success === false && data.message === "Incorrect password"){
      messageElement.textContent = "Incorrect password";
      messageElement.style.color = "red";
    } 
    else {
      messageElement.textContent = "User does not exist.";
      messageElement.style.color = "red";
    }

    //Append the message to the modal 
    const modalContent = document.querySelector("#loginModal .modal-content");
    const existingMessage = modalContent.querySelector("p.message");
    if (existingMessage) {
      existingMessage.remove();
    }
    messageElement.classList.add("message");
    modalContent.appendChild(messageElement);
  })
  .catch(error => console.error("Error during login:", error));
};


// Signup form submission
document.getElementById("signupFormSubmit").onclick = function(event) {
  event.preventDefault(); // Prevent form submission

  const email = document.getElementById("signupEmailField").value;
  const username = document.getElementById("signupUsernameField").value;
  const password = document.getElementById("signupPasswordField").value;
  const confirmPassword = document.getElementById("signupConfirmPasswordField").value;

  // Send the signup request to the backend
  fetch('/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, username, password, confirmPassword}),
  })
  .then(response => response.json())
  .then(data => {
    const messageElement = document.createElement("p");
    messageElement.style.textAlign = "center";

    if (data.success) {
      // Signup successful
      messageElement.textContent = "Signup successful!";
      messageElement.style.color = "green";
      // Close the modal after a delay
      setTimeout(() => {
        window.location.href = "/";
      }, 1000);
    }
    else if (data.success === false && data.message === "Username and password are required"){
      messageElement.textCaontent = "Username and password are required";
      messageElement.style.color = "red";
    }
    else if (data.success === false && data.message == "Username already taken"){
      messageElement.textContent = "Username already taken";
      messageElement.style.color = "red";
    } 
    else if (data.success === false && data.message == "User already exists"){
      messageElement.textContent = "User already exists";
      messageElement.style.color = "red";
    }
    else if (data.success === false && data.message == "Passwords do not match!"){
      messageElement.textContent = "Passwords do not match!";
      messageElement.style.color = "red";
    }
    else {
      // Signup failed
      messageElement.textContent = data.message;
      messageElement.style.color = "red";
    }

    // Append the message to the modal content
    const modalContent = document.querySelector("#createAccountModal .modal-content");
    const existingMessage = modalContent.querySelector("p.message");
    if (existingMessage) {
      existingMessage.remove();
    }
    messageElement.classList.add("message");
    modalContent.appendChild(messageElement);
  })
  .catch(error => console.error("Error during signup:", error));
};