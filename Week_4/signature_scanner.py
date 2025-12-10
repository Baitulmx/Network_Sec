import os
import re
# Define suspicious signatures to check for
SIGNATURES = [
    r"eval\(",
    r"base64\.b64decode",
    r"socket\.connect",
    r"exec\(",
    r"import os"
]
# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, "files_to_monitor")

for fname in os.listdir(folder):
    path = os.path.join(folder, fname)

    if os.path.isfile(path):
        with open(path, "r", errors="ignore") as f:
            data = f.read()

        print(f"\nScanning {fname}...")
        # Check for each signature
        for sig in SIGNATURES:
            if re.search(sig, data):
                print(f"  ⚠️ Suspicious signature found: {sig}")
