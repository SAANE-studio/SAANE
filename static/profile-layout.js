const profileLocalNav = document.querySelector(".profile-local-nav");

if (profileLocalNav && "IntersectionObserver" in window) {
  const sectionLinks = Array.from(profileLocalNav.querySelectorAll("a"));
  const profileSections = sectionLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  const observer = new IntersectionObserver(
    (entries) => {
      const visibleEntry = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

      if (!visibleEntry) {
        return;
      }

      sectionLinks.forEach((link) => {
        link.classList.toggle(
          "is-active",
          link.getAttribute("href") === `#${visibleEntry.target.id}`,
        );
      });
    },
    {
      rootMargin: "-38% 0px -46% 0px",
      threshold: [0, 0.2, 0.45, 0.7],
    },
  );

  profileSections.forEach((section) => observer.observe(section));
}

const profileIntroStage = document.querySelector(".profile-intro-spread");

if (profileIntroStage) {
  const portrait = profileIntroStage.querySelector(".profile-portrait img");
  const description = profileIntroStage.querySelector(".profile-intro-copy");
  let geometryFrame = 0;
  let resizeTimer;

  if (portrait) {
    portrait.addEventListener(
      "error",
      () => {
        const fallback = portrait.dataset.fallback;

        if (fallback && portrait.src !== new URL(fallback, document.baseURI).href) {
          portrait.src = fallback;
        }
      },
      { once: true },
    );
  }

  const updateCompositionGeometry = () => {
    if (
      !portrait ||
      !description ||
      window.matchMedia("(max-width: 760px)").matches
    ) {
      return;
    }

    const positioningRect = description.offsetParent?.getBoundingClientRect();

    if (!positioningRect) {
      return;
    }

    const portraitRect = portrait.getBoundingClientRect();
    const descriptionRect = description.getBoundingClientRect();
    const preferredTop = portraitRect.top + portraitRect.height * (2 / 3);
    const earliestTop = portraitRect.top + portraitRect.height * 0.5;
    const fitTop = portraitRect.bottom - descriptionRect.height - 16;
    const descriptionTop = Math.max(
      earliestTop,
      Math.min(preferredTop, fitTop),
    );

    profileIntroStage.style.setProperty(
      "--profile-description-y",
      `${descriptionTop - positioningRect.top}px`,
    );
    profileIntroStage.style.setProperty(
      "--profile-brand-center-y",
      `${portraitRect.top + portraitRect.height / 3 - positioningRect.top}px`,
    );
  };

  const scheduleCompositionGeometry = () => {
    window.cancelAnimationFrame(geometryFrame);
    geometryFrame = window.requestAnimationFrame(updateCompositionGeometry);
  };

  if (portrait) {
    if (portrait.complete) {
      scheduleCompositionGeometry();
    } else {
      portrait.addEventListener("load", scheduleCompositionGeometry, {
        once: true,
      });
    }

    if ("ResizeObserver" in window) {
      const resizeObserver = new ResizeObserver(scheduleCompositionGeometry);
      resizeObserver.observe(portrait);
      resizeObserver.observe(description);
    } else {
      window.addEventListener(
        "resize",
        () => {
          window.clearTimeout(resizeTimer);
          resizeTimer = window.setTimeout(scheduleCompositionGeometry, 120);
        },
        { passive: true },
      );
    }
  }

  if (document.fonts) {
    document.fonts.ready.then(scheduleCompositionGeometry);
  }

  window.addEventListener("load", scheduleCompositionGeometry);
}
