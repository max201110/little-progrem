import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]


def test_number_guessing_starts():
    result = subprocess.run(
        [sys.executable, str(ROOT / "number-guessing" / "main.py")],
        input="q\n", text=True, capture_output=True, check=True,
    )
    assert "The number was" in result.stdout


def test_todo_cli_add_and_list(tmp_path):
    source = ROOT / "todo-cli" / "todo.py"
    # Run in a copied folder so the repository remains free of generated data.
    target = tmp_path / "todo.py"
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    subprocess.run([sys.executable, str(target), "add", "demo"], check=True)
    result = subprocess.run([sys.executable, str(target), "list"], text=True, capture_output=True, check=True)
    assert "demo" in result.stdout
