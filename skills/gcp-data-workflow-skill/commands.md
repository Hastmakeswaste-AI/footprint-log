Usage examples (copy into Copilot chat or skill handlers):

- "Scaffold workflow for dataset sales_2026 --create-skeleton"
  -> creates repo structure, modeling template, CI file, and pipeline placeholder.

- "Show modeling template for dataset sales_2026"
  -> opens modeling_design_template.md with sections to fill.

Developer notes:
- Keep modeling design in repo/modeling/<dataset>/design.md and require sign-off before merging.
- CI should run unit tests and sample end-to-end job on staging sample data.
