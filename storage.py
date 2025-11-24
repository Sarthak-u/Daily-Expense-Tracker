# storage.py
import csv, os

def ensure(path, headers):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

def read_rows(path):
    ensure(path, ["id","title","amount","category","date","tag"])
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def write_rows(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id","title","amount","category","date","tag"])
        writer.writeheader()
        writer.writerows(rows)

def next_id(rows):
    return str(max([int(r["id"]) for r in rows], default=0) + 1)
