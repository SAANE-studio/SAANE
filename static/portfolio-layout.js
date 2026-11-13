const portfolioScroller = document.querySelector(".toc-section");

if (portfolioScroller) {
  const updateScrollHint = () => {
    const remainingScroll =
      portfolioScroller.scrollWidth -
      portfolioScroller.clientWidth -
      portfolioScroller.scrollLeft;

    portfolioScroller.classList.toggle(
      "has-right-overflow",
      remainingScroll > 1,
    );
  };

  portfolioScroller.addEventListener("scroll", updateScrollHint, {
    passive: true,
  });
  window.addEventListener("resize", updateScrollHint, { passive: true });
  updateScrollHint();
}
