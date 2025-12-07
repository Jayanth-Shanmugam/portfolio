function showSection(sectionId) {
  const sections = document.querySelectorAll(".section");
  const navLinks = document.querySelectorAll(".nav-link");

  sections.forEach((section) => {
    section.classList.remove("active");
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");
  });

  document.getElementById(sectionId).classList.add("active");

  const activeLink = document.querySelector(
    `[onclick="showSection('${sectionId}')"]`,
  );
  if (activeLink) {
    activeLink.classList.add("active");
  }

  window.scrollTo({ top: 0, behavior: "smooth" });
}

document.querySelectorAll(".nav-link").forEach((link) => {
  link.addEventListener("click", function (e) {
    e.preventDefault();
  });
});
