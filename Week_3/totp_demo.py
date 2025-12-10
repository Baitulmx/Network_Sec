import pyotp
import qrcode
# Generate a TOTP secret
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

print("Your secret:", secret)
print("Current OTP:", totp.now())

# Create provisioning URI
uri = totp.provisioning_uri(name="student@example.com", issuer_name="Goldsmiths NSSec")

# Generate QR
img = qrcode.make(uri)
img.save("totp_qr.png")
print("QR saved as totp_qr.png — Scan with Google Authenticator!")

while True:
    code = input("Enter OTP: ")
    if totp.verify(code):
        print("✔️ OTP valid!")
    else:
        print("❌ Invalid OTP!")
