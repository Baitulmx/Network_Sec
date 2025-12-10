import hashlib
import os
import csv
# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, "files_to_monitor")
baseline_csv = os.path.join(BASE_DIR, "baseline.csv")

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

# Load baseline
baseline = {}
with open(baseline_csv, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        baseline[row["filename"]] = row["sha256"]

# Detect changes
for fname in os.listdir(folder):
    full_path = os.path.join(folder, fname)

    if os.path.isfile(full_path):
        new_hash = hash_file(full_path)

        if fname not in baseline:
            print(f"[NEW FILE] {fname} was added.")
        elif baseline[fname] != new_hash:
            print(f"[MODIFIED] {fname} has changed!")
        else:
            print(f"[OK] {fname} unchanged.")

# Detect deleted files
for fname in baseline:
    if fname not in os.listdir(folder):
        print(f"[DELETED] {fname} was removed!")
