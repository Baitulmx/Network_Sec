import re
# I do not know what to do for sample as i dont want to push an .exe ad github could flag it as dangerous 
sample = r"C:\Users\soubh\Downloads\Procmon.exe"
# Function to extract printable strings
def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    return re.findall(rb"[ -~]{4,}", data)
# Print first 50 strings
for s in extract_strings(sample)[:50]:
    print(s.decode(errors="ignore"))
