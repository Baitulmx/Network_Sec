import hashlib
# I do not know what to do for sample as i dont want to push an .exe ad github could flag it as dangerous 
sample = r"C:\Users\soubh\Downloads\Procmon.exe"
# Function to compute hash
def compute_hash(file_path, algo):
    h = hashlib.new(algo)
    with open(file_path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

print("MD5:   ", compute_hash(sample, "md5"))
print("SHA1:  ", compute_hash(sample, "sha1"))
print("SHA256:", compute_hash(sample, "sha256"))
