import string
import math

bad_passwords = ["password", "123456", "qwerty", "letmein", "admin"]

def password_entropy(password, pool_size):
    return len(password) * math.log2(pool_size)

def check_password_strength(password):
    score = 0
    pool_size = 0

    # Length checks
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character set checks
    if any(c.islower() for c in password):
        score += 1
        pool_size += 26
    if any(c.isupper() for c in password):
        score += 1
        pool_size += 26
    if any(c.isdigit() for c in password):
        score += 1
        pool_size += 10
    if any(c in string.punctuation for c in password):
        score += 1
        pool_size += len(string.punctuation)

    # Check against known weak passwords
    if password.lower() in bad_passwords:
        score = 0

    entropy = password_entropy(password, pool_size)

    return score, entropy

# Demo
password = input("Enter a password to test: ")
score, entropy = check_password_strength(password)

print(f"Score: {score}/6")
print(f"Entropy: {entropy:.2f} bits")