document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("themeToggle");
  const body = document.body;

  if (!toggle) return;

  // Load saved theme
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    body.className = savedTheme;
    toggle.textContent = savedTheme === "dark-theme" ? "☀️ Light Mode" : "🌙 Dark Mode";
  } else {
    // default light theme
    body.className = "light-theme";
    toggle.textContent = "🌙 Dark Mode";
  }

  toggle.addEventListener("click", () => {
    if (body.classList.contains("light-theme")) {
      body.classList.replace("light-theme", "dark-theme");
      localStorage.setItem("theme", "dark-theme");
      toggle.textContent = "☀️ Light Mode";
    } else {
      body.classList.replace("dark-theme", "light-theme");
      localStorage.setItem("theme", "light-theme");
      toggle.textContent = "🌙 Dark Mode";
    }
  });
});
