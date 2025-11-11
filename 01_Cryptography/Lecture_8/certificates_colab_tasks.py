import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# --- Practical Task 1: Generating and Inspecting a Self-Signed Certificate ---

print("--- Task 1: Generating and Inspecting a Self-Signed Certificate ---")

# 1. Generate an RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# 2. Define the certificate's subject and issuer
# For a self-signed certificate, the subject and issuer are the same.
subject = issuer = x509.Name(
    [
        x509.NameAttribute(NameOID.COUNTRY_NAME, "UK"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "London"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "London"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My University"),
        x509.NameAttribute(NameOID.COMMON_NAME, "my-test-site.com"),
    ]
)

# 3. Build the certificate
cert_builder = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(public_key)
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(
        # Certificate will be valid for 30 days
        datetime.datetime.utcnow()
        + datetime.timedelta(days=30)
    )
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName("localhost")]),
        critical=False,
    )
)

# 4. Sign the certificate with the private key
self_signed_cert = cert_builder.sign(private_key, hashes.SHA256())

# 5. Save the certificate to a file (optional, but good practice)
with open("self_signed_certificate.pem", "wb") as f:
    f.write(self_signed_cert.public_bytes(serialization.Encoding.PEM))

print("Self-signed certificate generated successfully.")

# 6. Inspect the certificate's fields
print("\n--- Inspecting Certificate Details ---")
print(f"Subject: {self_signed_cert.subject.rfc4514_string()}")
print(f"Issuer: {self_signed_cert.issuer.rfc4514_string()}")
print(f"Serial Number: {self_signed_cert.serial_number}")
print(f"Valid From: {self_signed_cert.not_valid_before}")
print(f"Valid Until: {self_signed_cert.not_valid_after}")


# --- Practical Task 2: Creating and Verifying Digital Signatures ---

print("\n--- Task 2: Creating and Verifying a Digital Signature ---")

# 1. Define a message to sign
message_to_sign = b"This is a very important document that needs to be signed."

# 2. Create the digital signature
signature = private_key.sign(
    message_to_sign,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

print(f"Original Message: {message_to_sign.decode()}")
print(f"Digital Signature (first 32 bytes): {signature[:32].hex()}...")

# 3. Verify the signature with the public key
print("\n--- Verifying the Signature ---")
try:
    public_key.verify(
        signature,
        message_to_sign,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    print("Signature is VALID. The message has not been tampered with.")
except Exception as e:
    print(f"Signature is INVALID. Verification failed: {e}")

# 4. Demonstrate a verification failure with a tampered message
print("\n--- Attempting to Verify a Tampered Message ---")
tampered_message = b"This is a very important document that has been tampered with."

try:
    public_key.verify(
        signature,
        tampered_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    print("Signature is VALID.")
except Exception as e:
    print(
        f"Signature is INVALID. As expected, verification failed for the tampered message."
    )
