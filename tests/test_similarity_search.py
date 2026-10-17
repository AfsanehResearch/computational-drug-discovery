import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "03-Cheminformatics" / "similarity_search.py"
CSV_FILE = ROOT / "03-Cheminformatics" / "similarity_results.csv"


def test_similarity_search_runs_successfully():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert "Molecular Screening Results" in result.stdout
    assert "Similarity: 1.000" in result.stdout


def test_similarity_results_csv():
    assert CSV_FILE.exists(), "CSV output file was not created"

    with CSV_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 5

    expected_columns = {
        "SMILES",
        "Tanimoto_Similarity",
        "Molecular_Weight",
        "LogP",
        "H_Bond_Donors",
        "H_Bond_Acceptors",
        "TPSA",
    }
    assert expected_columns.issubset(rows[0].keys())

    similarities = [
        float(row["Tanimoto_Similarity"]) for row in rows
    ]
    assert similarities == sorted(similarities, reverse=True)
    assert similarities[0] == 1.0