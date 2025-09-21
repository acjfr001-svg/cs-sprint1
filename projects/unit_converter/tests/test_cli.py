import os, sys, subprocess, pathlib

# Point PYTHONPATH to .../projects/unit_converter (the folder that contains the "unit_converter" package)
PKG_BASE = pathlib.Path(__file__).resolve().parents[1]
ENV = os.environ.copy()
ENV["PYTHONPATH"] = str(PKG_BASE)

def run_cmd(args):
    return subprocess.run(args, capture_output=True, text=True, env=ENV)

def test_cli_c_to_f():
    r = run_cmd([sys.executable, "-m", "unit_converter", "--from", "C", "--to", "F", "--value", "100"])
    assert r.returncode == 0, r.stderr + r.stdout
    assert float(r.stdout.strip()) == 212.0

def test_cli_unsupported():
    r = run_cmd([sys.executable, "-m", "unit_converter", "--from", "C", "--to", "K", "--value", "0"])
    assert r.returncode != 0
    assert "Unsupported conversion" in (r.stderr + r.stdout)
