(() => {
  const toggle = document.querySelector(".mobile-menu-toggle");
  const menu = document.querySelector("#mobile-menu");
  if (!toggle || !menu) return;
  const mobile = window.matchMedia("(max-width: 760px)");
  const close = () => { if (menu.open) menu.close(); };
  toggle.addEventListener("click", () => {
    if (!mobile.matches) return;
    menu.hidden = false;
    menu.showModal();
    toggle.setAttribute("aria-expanded", "true");
    document.documentElement.classList.add("mobile-menu-open");
  });
  menu.querySelector(".mobile-menu-close").addEventListener("click", close);
  menu.querySelectorAll("a").forEach(link => link.addEventListener("click", close));
  menu.addEventListener("keydown", event => {
    if (event.key !== "Tab") return;
    const items = [...menu.querySelectorAll("button, a[href]")];
    const first = items[0], last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault(); last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault(); first.focus();
    }
  });
  menu.addEventListener("close", () => {
    menu.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
    document.documentElement.classList.remove("mobile-menu-open");
    if (mobile.matches) toggle.focus();
  });
  mobile.addEventListener("change", () => { if (!mobile.matches) close(); });
  window.addEventListener("pagehide", close);

  const select = document.querySelector("#mobile-research-category");
  if (select) {
    const filters = [...document.querySelectorAll("[data-research-filter]")];
    const sync = () => {
      const active = filters.find(button => button.classList.contains("is-active"));
      if (active) select.value = active.dataset.researchFilter;
    };
    select.addEventListener("change", () => filters.find(button => button.dataset.researchFilter === select.value)?.click());
    filters.forEach(button => button.addEventListener("click", () => queueMicrotask(sync)));
    sync();
  }
})();