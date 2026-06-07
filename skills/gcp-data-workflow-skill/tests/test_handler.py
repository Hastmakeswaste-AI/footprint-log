import os
import sys
import subprocess
import tempfile

def test_scaffold_creates_files():
    tmp = tempfile.mkdtemp()
    handler = os.path.join(os.path.dirname(__file__), '..', 'handler.py')
    # run handler in temp dir
    res = subprocess.run([sys.executable, handler, 'scaffold', 'test_dataset'], cwd=tmp)
    assert res.returncode == 0
    outdir = os.path.join(tmp, 'workflows', 'test_dataset')
    assert os.path.isdir(outdir)
    assert os.path.isfile(os.path.join(outdir, 'design.md'))
