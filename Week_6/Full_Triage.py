import hashlib, pefile, re, yara
# I do not know what to do for sample as i dont want to push an .exe ad github could flag it as dangerous 
sample = r"C:\Users\soubh\Downloads\Procmon.exe"
# Function to compute multiple hashes
def compute_hashes(path):
    algos = ["md5", "sha1", "sha256"]
    output = {}
    for a in algos:
        h = hashlib.new(a)
        with open(path, "rb") as f:
            h.update(f.read())
        output[a] = h.hexdigest()
    return output
# Function to extract printable strings
def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    return re.findall(rb"[ -~]{4,}", data)

print("Hashes:", compute_hashes(sample))

print("\nStrings:")
print(extract_strings(sample)[:10])

print("\nImports:")
pe = pefile.PE(sample)
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print(entry.dll.decode())
# Extract Indicators of Compromise (IOCs)
print("\nIOCs:")
decoded = open(sample, "rb").read().decode(errors="ignore")
print("URLs:", re.findall(r"https?://[^\s\"']+", decoded))
print("IPs:", re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", decoded))
# YARA scanning
print("\nYARA:")
rule = yara.compile(source="""
rule Simple {
    strings: $s = "http"
    condition: $s
}
""")
print(rule.match(sample))
