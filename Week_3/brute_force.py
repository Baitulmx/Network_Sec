import hashlib
import time

common_passwords = ["password", "123456", "letmein", "qwerty", "admin"]
# Brute-force hash cracker
def crack_hash(target_hash, algorithm="md5"):
    start = time.time()
    # Try each common password
    for pwd in common_passwords:
        if algorithm == "md5":
            attempt = hashlib.md5(pwd.encode()).hexdigest()
        elif algorithm == "sha256":
            attempt = hashlib.sha256(pwd.encode()).hexdigest()
        else:
            raise ValueError("Unsupported algorithm")
        # Check if hash matches
        if attempt == target_hash:
            end = time.time()
            print(f"FOUND! Password = {pwd}")
            print(f"Time: {end - start:.6f} seconds")
            return True

    print("Not found.")
    return False

# Demo
hashed = hashlib.md5("password".encode()).hexdigest()
crack_hash(hashed, "md5")
