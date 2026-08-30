document.addEventListener("click", (event) => {
  document.querySelectorAll("details.email-pop[open]").forEach((panel) => {
    if (!panel.contains(event.target)) {
      panel.removeAttribute("open");
    }
  });
});
