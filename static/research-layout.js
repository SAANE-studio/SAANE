const researchCards = [...document.querySelectorAll(".research-card")];
const researchFilters = [
  ...document.querySelectorAll("[data-research-filter]"),
];
const researchEmptyState = document.querySelector(".research-empty-state");

researchFilters.forEach((filter) => {
  filter.addEventListener("click", () => {
    if (filter.dataset.researchUrl) { window.location.assign(filter.dataset.researchUrl); return; }
    const selectedCategory = filter.dataset.researchFilter;
    let visibleCardCount = 0;

    researchFilters.forEach((button) => {
      const isActive = button === filter;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", String(isActive));
    });

    researchCards.forEach((card) => {
      const isVisible =
        selectedCategory === "all" ||
        card.dataset.researchCategory === selectedCategory;

      card.classList.toggle("is-hidden", !isVisible);
      if (isVisible) {
        visibleCardCount += 1;
      }
    });

    if (researchEmptyState) {
      researchEmptyState.hidden = visibleCardCount > 0;
    }
  });
});

const initialCategory = new URLSearchParams(window.location.search).get('category');
if (initialCategory) { researchFilters.find((button) => button.dataset.researchFilter === initialCategory && !button.dataset.researchUrl)?.click(); }

