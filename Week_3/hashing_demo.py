import hashlib
import bcrypt

password = input("Enter password: ").encode()

# MD5
md5_hash = hashlib.md5(password).hexdigest()

# SHA-256
sha_hash = hashlib.sha256(password).hexdigest()

# bcrypt
bcrypt_hash = bcrypt.hashpw(password, bcrypt.gensalt())

print("\n HASH RESULTS")
print("MD5:      ", md5_hash)
print("SHA-256:  ", sha_hash)
print("bcrypt:   ", bcrypt_hash.decode())
