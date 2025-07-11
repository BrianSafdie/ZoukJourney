window.addEventListener("DOMContentLoaded", () => {
  const userName = localStorage.getItem("userName");

  if (!userName) {
    window.location.href = "index.html";
  } else {
    const greetingEl = document.getElementById("greeting");
    if (greetingEl) {
      greetingEl.innerText = `👋 Hello, ${userName}`;
    }
    document.body.classList.remove("hidden-body");
  }
});