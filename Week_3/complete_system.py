import bcrypt
import pyotp
import string
import math
import qrcode   # ← added for QR code support

# Password strength and entropy calculation
def password_entropy(password, pool_size):
    return len(password) * math.log2(pool_size)
# password strength scoring
def password_strength(password):
    score = 0
    pool = 0
    # Basic checks
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.islower() for c in password): score += 1; pool += 26
    if any(c.isupper() for c in password): score += 1; pool += 26
    if any(c.isdigit() for c in password): score += 1; pool += 10
    if any(c in string.punctuation for c in password): score += 1; pool += len(string.punctuation)
    # Calculate entropy
    entropy = password_entropy(password, pool)
    return score, entropy

# Complete authentication system
class AuthSystem:
    def __init__(self):
        self.users = {}
    # Register user with hashed password and TOTP
    def register_user(self, username, password):
        score, entropy = password_strength(password)
        if score < 4:
            raise ValueError("Weak password!")
        # Hash password with bcrypt
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        totp_secret = pyotp.random_base32()
        # Store user data
        self.users[username] = {"hash": hashed, "totp": totp_secret}
        print("User registered!")

        # TOTP provisioning URI
        uri = pyotp.TOTP(totp_secret).provisioning_uri(username, issuer_name="NSSec")
        print("Scan this QR in Google Authenticator:")
        print(uri)

        # Generate and save QR code as .png file
        img = qrcode.make(uri)
        filename = f"{username}_totp.png"
        img.save(filename)
        print(f"QR code saved as {filename}")
        
    # Authenticate user with password and TOTP
    def authenticate(self, username, password, otp):
        if username not in self.users:
            return False
        # Retrieve stored hash and TOTP secret
        stored_hash = self.users[username]["hash"]
        totp_secret = self.users[username]["totp"]
        # Verify password
        if not bcrypt.checkpw(password.encode(), stored_hash):
            return False
        # Verify TOTP
        totp = pyotp.TOTP(totp_secret)
        return totp.verify(otp)


# Demo
auth = AuthSystem()
auth.register_user("Soub", "MyP@ssw0rd!!")

otp = input("Enter OTP: ")
print("Authenticated:", auth.authenticate("Soub", "MyP@ssw0rd!!", otp))
