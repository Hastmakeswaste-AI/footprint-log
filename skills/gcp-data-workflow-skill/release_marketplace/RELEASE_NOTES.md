Release Notes - GCP Data Workflow Skill v0.1.0

Overview:
This release provides a lightweight Copilot skill that scaffolds a dataset workflow for Tier0->Tier1 on GCP. Intended for internal teams and early adopters.

What to expect:
- Quick scaffold: creates workflows/<dataset>/ with design.md, sample_transform.py and cloudbuild.yaml
- Modeling template requires manual completion and sign-off
- Included pytest to validate scaffold behavior

Known limitations:
- Pipeline is a placeholder; replace with Dataflow/Beam or dbt as needed
- No automatic deployment to BigQuery included in this initial version
