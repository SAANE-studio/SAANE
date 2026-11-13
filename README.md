# SAANE

Hugo source for the SAANE portfolio and Learnings pages.

## Local preview

Install Hugo Extended and Python 3.10+ with PyYAML. For Hugo-only preview, run:

    hugo server --renderToMemory

For Obsidian autosync, configure the local, ignored `scripts/obsidian-publication.json` and run `preview-saane.cmd`. See `docs/obsidian-autosync.md`.

Edit source files in `content`, `data`, `layouts`, and `static`. Do not edit generated files in `public`.

## Publication status

Uploading this repository does not deploy a website. No deployment workflow is included.
Before enabling GitHub Pages, configure the final baseURL (`https://USERNAME.github.io/saane/`), verify subdirectory image/link paths, and apply site-wide noindex as requested. The current local configuration is not yet prepared for public deployment.

The Obsidian vault, local configuration, preview backups, and generated output are excluded from Git.
