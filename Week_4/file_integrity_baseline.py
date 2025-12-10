import hashlib
import os
import csv
from datetime import datetime
# hash a file
def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()
# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, "files_to_monitor")   # create this folder and put files in it
baseline_csv = os.path.join(BASE_DIR, "baseline.csv")

with open(baseline_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "sha256", "timestamp"])

    for fname in os.listdir(folder):
        full_path = os.path.join(folder, fname)

        if os.path.isfile(full_path):
            file_hash = hash_file(full_path)
            timestamp = datetime.now().isoformat()

            writer.writerow([fname, file_hash, timestamp])

print("Baseline created and saved to baseline.csv")
