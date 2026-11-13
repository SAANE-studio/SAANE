# Obsidian autosync
Run preview-saane.cmd. Requires Hugo, Python 3.10+, and PyYAML (already installed on this computer).
Notes anywhere in the configured vault are included when YAML Properties contain publish: true and website_section: research. Required: title, slug (unique lowercase kebab-case), category. Optional: summary, date, article_type, cover, description, tags.
Place --- on the very first line for Obsidian Properties. The importer tolerates preceding blank lines without changing the source.
Only referenced attachments are copied. A missing/ambiguous reference or duplicate slug blocks that sync batch; the prior website remains available. Only publish-approved notes can be embedded or linked as notes.
Metadata follows Obsidian. If date is absent the original generated date is retained. If cover is absent the existing cover, first imported image, or SAANE logo is used.
Changing publish to false or removing Properties marks previously auto-managed outputs as drafts. No files are deleted. Do not change a published slug without explicitly migrating its output.
Existing manually managed articles are never overwritten by discovered notes. Natural Ventilation retains its original explicit manifest authorization until Properties take over.
The watcher waits for saves to settle, then syncs. Keep its terminal open. It reuses an existing local server. This does not deploy anything to the internet.
Backups and managed-note ownership are stored in .saane-preview/. The vault is never edited.
