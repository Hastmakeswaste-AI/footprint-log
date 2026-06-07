GCP Data Workflow Skill

Overview

This Copilot skill scaffolds a complete dataset workflow skeleton for GCP Tier0→Tier1 pipelines. It creates a modeling design template (for human modelers), a pipeline placeholder (sample_transform.py), and a CI sample (cloudbuild.yaml). The skill accelerates onboarding and enforces a standard repo layout for datasets.

Features
- Create workflows/<dataset>/ with design.md, sample_transform.py and cloudbuild.yaml
- Modeling template with input schema, mapping rules, DQ checks and acceptance criteria
- CI sample running pytest for scaffold validation
- Sample T0 CSV for testing

Usage
- Install: copilot plugin install <zip_or_path>
- Scaffold: in skill folder run `python handler.py scaffold <dataset_name>` or use the Copilot command once installed

Notes & Limitations
- The transformation is a placeholder; replace with Dataflow/Beam, dbt or BigQuery SQL for production
- Modeling design must be completed and signed off by a human modeler before deployment

Support & Licensing
- License: MIT (placeholder)
- Support: support@your-company.example.com
