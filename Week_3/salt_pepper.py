import os
import hashlib
# Define a constant PEPPER
PEPPER = "TypeBeatPepper"

def simple_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def salted_hash(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

password = "user123password"

# 1 Without Salt
no_salt_1 = simple_hash(password)
no_salt_2 = simple_hash(password)

# 2 With Salt
salt1 = os.urandom(16).hex()
salt2 = os.urandom(16).hex()

with_salt_1 = salted_hash(password, salt1)
with_salt_2 = salted_hash(password, salt2)

# 3 With Pepper
peppered = simple_hash(password + PEPPER)

print("\nNO SALT:")
print(no_salt_1)
print(no_salt_2)

print("\nWITH SALT:")
print(with_salt_1)
print(with_salt_2)

print("\nWITH PEPPER:")
print(peppered)
