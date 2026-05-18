// ========================================
// Authentication Page Logic
// ========================================

const API_BASE = "https://linkedinassitantapi.hnhsofttechsolutions.com";
// const API_BASE = "http://localhost:9011";

// Check if token exists and redirect, then wire up all button listeners
window.addEventListener("DOMContentLoaded", () => {
  // Wire up button event listeners (no inline onclick — blocked by extension CSP)
  document.getElementById("loginBtn").addEventListener("click", handleLogin);
  document.getElementById("registerBtn").addEventListener("click", handleRegister);
  document.getElementById("toggleFormLink").addEventListener("click", (e) => {
    e.preventDefault();
    toggleForm();
  });
  document.getElementById("createAdminBtn").addEventListener("click", toggleForm);

  // Allow pressing Enter in login fields to submit
  document.getElementById("password").addEventListener("keydown", (e) => {
    if (e.key === "Enter") handleLogin();
  });
  document.getElementById("regPasswordConfirm").addEventListener("keydown", (e) => {
    if (e.key === "Enter") handleRegister();
  });

  // Check existing auth state
  chrome.storage.local.get(["auth_token"], (result) => {
    const token = result.auth_token;
    if (token) {
      verifyToken(token)
        .then(() => {
          window.location.href = "./index.html";
        })
        .catch(() => {
          chrome.storage.local.remove("auth_token");
          showLoginForm();
        });
    } else {
      checkIfAdminExists();
    }
  });
});

// Check if admin exists
async function checkIfAdminExists() {
  try {
    const response = await fetch(`${API_BASE}/admin/auth/verify`, {
      headers: { "Authorization": "Bearer dummy-token" }
    });

    if (response.status === 401 || response.status === 403) {
      showLoginForm();
    }
  } catch (err) {
    showLoginForm();
  }
}

// Verify JWT token
async function verifyToken(token) {
  const response = await fetch(`${API_BASE}/admin/auth/verify`, {
    headers: { "Authorization": `Bearer ${token}` }
  });

  if (!response.ok) throw new Error("Invalid token");
  return response.json();
}

// Show login form
function showLoginForm() {
  document.getElementById("loginForm").style.display = "block";
  document.getElementById("registerForm").style.display = "none";
  document.getElementById("noAdminMessage").style.display = "none";
}

// Toggle between login and register
function toggleForm() {
  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");

  if (loginForm.style.display === "none") {
    loginForm.style.display = "block";
    registerForm.style.display = "none";
  } else {
    loginForm.style.display = "none";
    registerForm.style.display = "block";
  }
}

// Handle login
async function handleLogin() {
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const errorDiv = document.getElementById("loginError");

  errorDiv.textContent = "";
  errorDiv.classList.remove("show");

  if (!username || !password) {
    errorDiv.textContent = "Please enter both username and password";
    errorDiv.classList.add("show");
    return;
  }

  const loginBtn = document.getElementById("loginBtn");
  loginBtn.disabled = true;
  loginBtn.textContent = "Logging in...";

  try {
    const response = await fetch(`${API_BASE}/admin/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (!response.ok) {
      errorDiv.textContent = data.detail || "Login failed";
      errorDiv.classList.add("show");
      loginBtn.disabled = false;
      loginBtn.textContent = "Login";
      return;
    }

    // Store token in chrome.storage.local so the extension can access it
    chrome.storage.local.set({
      auth_token: data.access_token,
      user_id: data.user_id,
      username: data.username
    }, () => {
      window.location.href = "./index.html";
    });
  } catch (err) {
    errorDiv.textContent = "Connection error: " + err.message;
    errorDiv.classList.add("show");
    loginBtn.disabled = false;
    loginBtn.textContent = "Login";
  }
}

// Handle register
async function handleRegister() {
  const username = document.getElementById("regUsername").value.trim();
  const password = document.getElementById("regPassword").value.trim();
  const passwordConfirm = document.getElementById("regPasswordConfirm").value.trim();
  const errorDiv = document.getElementById("registerError");

  errorDiv.textContent = "";
  errorDiv.classList.remove("show");

  if (!username || !password || !passwordConfirm) {
    errorDiv.textContent = "All fields are required";
    errorDiv.classList.add("show");
    return;
  }

  if (username.length < 3) {
    errorDiv.textContent = "Username must be at least 3 characters";
    errorDiv.classList.add("show");
    return;
  }

  if (password.length < 6) {
    errorDiv.textContent = "Password must be at least 6 characters";
    errorDiv.classList.add("show");
    return;
  }

  if (password !== passwordConfirm) {
    errorDiv.textContent = "Passwords do not match";
    errorDiv.classList.add("show");
    return;
  }

  const registerBtn = document.getElementById("registerBtn");
  registerBtn.disabled = true;
  registerBtn.textContent = "Creating account...";

  try {
    const response = await fetch(`${API_BASE}/admin/auth/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (!response.ok) {
      errorDiv.textContent = data.detail || "Registration failed";
      errorDiv.classList.add("show");
      registerBtn.disabled = false;
      registerBtn.textContent = "Create Account";
      return;
    }

    // Store token in chrome.storage.local so the extension can access it
    chrome.storage.local.set({
      auth_token: data.access_token,
      user_id: data.user_id,
      username: data.username
    }, () => {
      window.location.href = "./index.html";
    });
  } catch (err) {
    errorDiv.textContent = "Connection error: " + err.message;
    errorDiv.classList.add("show");
    registerBtn.disabled = false;
    registerBtn.textContent = "Create Account";
  }
}
