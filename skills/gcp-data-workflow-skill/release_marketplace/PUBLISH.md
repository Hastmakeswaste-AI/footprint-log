Publishing checklist for Copilot Marketplace

1) Prepare assets
   - marketplace_manifest.json (metadata)
   - gcp-data-workflow-skill.zip (package)
   - README.md (usage & install)
   - LICENSE, CHANGELOG.md, RELEASE_NOTES.md
   - screenshots/ (3 PNGs: hero, scaffold example, CI run)
   - pricing.md, support.md

2) Quality checks
   - Run `pytest` in skill folder
   - Validate package installs via `copilot plugin install <path-to-zip>`
   - Verify handler scaffold command creates expected files

3) Versioning & release
   - Tag repository with v0.1.0
   - Upload ZIP to marketplace portal, attach manifest and assets
   - Fill marketing description and categories

4) Post-publish
   - Monitor install telemetry
   - Prepare support channel and SLA
   - Publish changelog and notify customers

Notes:
- Replace placeholder LICENSE and contact info before public release.
- Ensure no secrets are included in ZIP.
