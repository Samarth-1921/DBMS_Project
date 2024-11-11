function handleLogin(event) {

event.preventDefault(); // Prevent form submission

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === "student" && password === "12345") {
    alert("Login Successful!");
    window.location.href = "homepage.html"; // Redirect to Home Page after login
  } else {
    alert("Invalid username or password");
  }

}