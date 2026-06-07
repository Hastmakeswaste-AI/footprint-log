#!/usr/bin/env python3
"""Simple Copilot skill handler to scaffold a dataset workflow.
Usage: python handler.py scaffold <dataset_name>
This creates ./workflows/<dataset_name>/ with design.md, sample_transform.py and cloudbuild.yaml
"""
import os, sys, shutil

def scaffold(dataset):
    cwd = os.getcwd()
    out = os.path.join(cwd, 'workflows', dataset)
    os.makedirs(out, exist_ok=True)
    here = os.path.dirname(__file__)
    # copy modeling template
    tmpl = os.path.join(here, 'modeling_design_template.md')
    if os.path.exists(tmpl):
        with open(tmpl, 'r', encoding='utf-8') as f:
            content = f.read().replace('<dataset_name>', dataset)
        with open(os.path.join(out, 'design.md'), 'w', encoding='utf-8') as f:
            f.write(content)
    # copy sample transform
    src_transform = os.path.join(here, 'pipelines', 'sample_transform.py')
    if os.path.exists(src_transform):
        shutil.copy(src_transform, os.path.join(out, 'sample_transform.py'))
    # write CI snippet
    ci = """steps:
- name: 'gcr.io/cloud-builders/gcloud'
  args: ['bash', '-c', 'echo "Running unit tests" && python -m pytest -q']
- name: 'gcr.io/cloud-builders/gcloud'
  args: ['bash', '-c', 'echo "(placeholder) deploy pipeline to staging"']
"""
    with open(os.path.join(out, 'cloudbuild.yaml'), 'w', encoding='utf-8') as f:
        f.write(ci)
    print('Scaffolded workflow to', out)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: handler.py scaffold <dataset_name>')
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == 'scaffold':
        if len(sys.argv) < 3:
            print('Usage: handler.py scaffold <dataset_name>')
            sys.exit(2)
        scaffold(sys.argv[2])
    else:
        print('Unknown command:', cmd)
        sys.exit(2)
