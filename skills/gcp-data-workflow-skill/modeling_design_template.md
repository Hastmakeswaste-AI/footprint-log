# Modeling Design Template

Dataset: <dataset_name>
Source format: CSV / Parquet and example file names
T0 storage: GCS path (gs://<bucket>/tier0/<dataset>/v{version}/)
T1 target: BigQuery dataset.table

1) Purpose and owner
2) Input schema (fields, types, nullable)
3) Mapping rules (T0 -> T1) with examples
4) Transformation logic (detailed SQL/pseudocode)
5) Data Quality rules (DQ checks with thresholds)
6) Test cases (sample inputs and expected outputs)
7) Performance expectations and SLAs
8) Acceptance criteria and sign-off (modeler + data owner)
