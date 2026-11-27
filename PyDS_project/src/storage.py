"""storage.py – Lab 6: files, folders and saving results.

WHAT GOES HERE
    All paths of the project (with pathlib) and functions that save and read
    results: cleaned data to data/processed/, tables to results/tables/,
    figures to results/figures/. Other modules import the paths from here.

EXAMPLE (reference project – basketball shots)
    save_table(zone_summary, "zones.csv")   -> results/tables/zones.csv
    save_json({"rows": 218000}, "run.json") -> results/tables/run.json
    figure_path("court_heatmap.png")        -> results/figures/court_heatmap.png
"""

# Your code from Lab 6 goes below.
import csv
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
RESULTS_DIR = PROJECT_DIR / "results"
TABLES_DIR = RESULTS_DIR / "tables"


def ensure_folder(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def list_files(folder, pattern="*"):
    return sorted(p.name for p in Path(folder).glob(pattern))


def save_table(rows, filename, folder=TABLES_DIR):
    folder = ensure_folder(folder)
    path = folder / filename
    if not rows:
        path.write_text("", encoding="utf-8")
        return path
    fieldnames = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def load_table(filename, folder=TABLES_DIR):
    path = Path(folder) / filename
    with open(path, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_json(data, filename, folder=TABLES_DIR):
    folder = ensure_folder(folder)
    path = folder / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path


def load_json(filename, folder=TABLES_DIR):
    path = Path(folder) / filename
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
