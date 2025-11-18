from cryptography.hazmat.primitives.asymmetric import dh, ec, rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography import x509
from cryptography.x509.oid import NameOID
import os
import datetime

# --- Practical Task 1: Implementing Diffie-Hellman Key Exchange ---

print("--- Task 1: Implementing Classic Diffie-Hellman Key Exchange ---")

# 1. Generate DH parameters (p and g). In a real scenario, these might be pre-agreed.
# This can be slow, so for a live demo, you might use pre-generated parameters.
print("Generating DH parameters (p and g)... This may take a moment.")
parameters = dh.generate_parameters(generator=2, key_size=2048)
p = parameters.parameter_numbers().p
g = parameters.parameter_numbers().g
print("DH parameters generated.")

# 2. Alice generates her private and public keys
alice_private_key = parameters.generate_private_key()
alice_public_key_bytes = alice_private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# 3. Bob generates his private and public keys
bob_private_key = parameters.generate_private_key()
bob_public_key_bytes = bob_private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

print("\nAlice and Bob have generated their private/public key pairs.")

# 4. Alice and Bob exchange public keys and generate the shared secret
# Alice receives Bob's public key and computes the shared key
bob_public_key = serialization.load_pem_public_key(bob_public_key_bytes)
alice_shared_key = alice_private_key.exchange(bob_public_key)

# Bob receives Alice's public key and computes the shared key
alice_public_key = serialization.load_pem_public_key(alice_public_key_bytes)
bob_shared_key = bob_private_key.exchange(alice_public_key)

print(f"Alice's shared key (first 16 bytes): {alice_shared_key[:16].hex()}")
print(f"Bob's shared key (first 16 bytes):   {bob_shared_key[:16].hex()}")

# 5. Verify that the keys are identical
assert alice_shared_key == bob_shared_key
print("\nSuccess! Alice and Bob have independently generated the same shared secret.")

# --- Practical Task 2: Elliptic Curve Diffie-Hellman (ECDHE) ---

print("\n--- Task 2: Implementing Elliptic Curve Diffie-Hellman (ECDHE) ---")

# 1. Alice generates her ephemeral EC key pair
# Using SECP384R1, a commonly used curve
alice_ec_private_key = ec.generate_private_key(ec.SECP384R1())
alice_ec_public_key = alice_ec_private_key.public_key()

# 2. Bob generates his ephemeral EC key pair
bob_ec_private_key = ec.generate_private_key(ec.SECP384R1())
bob_ec_public_key = bob_ec_private_key.public_key()

print("Alice and Bob have generated their ephemeral Elliptic Curve key pairs.")

# 3. Alice and Bob exchange public keys and generate the shared secret
alice_ec_shared_key = alice_ec_private_key.exchange(ec.ECDH(), bob_ec_public_key)
bob_ec_shared_key = bob_ec_private_key.exchange(ec.ECDH(), alice_ec_public_key)

print(f"Alice's EC shared key (first 16 bytes): {alice_ec_shared_key[:16].hex()}")
print(f"Bob's EC shared key (first 16 bytes):   {bob_ec_shared_key[:16].hex()}")

# 4. Verify that the keys are identical
assert alice_ec_shared_key == bob_ec_shared_key
print("\nSuccess! ECDHE key exchange completed successfully.")

# --- Practical Task 3: Simulating a TLS Handshake ---

print("\n--- Task 3: Simulating the Cryptographic Core of a TLS Handshake ---")

# Step A: Server Setup (Certificate and Private Key)
# This reuses the logic from the previous lesson to create a self-signed certificate for the server.
server_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "myserver.com")])
server_cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(server_private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=10))
    .sign(server_private_key, hashes.SHA256())
)

print("Server has generated its private key and self-signed certificate.")

# Step B: Handshake Simulation

# 1. Client receives server's certificate and verifies it (conceptually)
# In a real scenario, the client would check the signature against a trusted CA store.
# Here, we just extract the public key for the next step.
server_public_key = server_cert.public_key()
print("Client has received and verified the server's certificate.")

# 2. Client and Server perform an ECDHE key exchange
client_ec_private_key = ec.generate_private_key(ec.SECP384R1())
client_ec_public_key = client_ec_private_key.public_key()
server_ec_private_key = ec.generate_private_key(ec.SECP384R1())
server_ec_public_key = server_ec_private_key.public_key()

# They exchange public keys to generate the shared secret (pre-master secret)
shared_secret = client_ec_private_key.exchange(ec.ECDH(), server_ec_public_key)
print("Client and Server have performed ECDHE and established a shared secret.")

# Step C: Session Key Derivation
# The shared secret is not used directly. It's fed into a Key Derivation Function (KDF).
# HKDF is a standard KDF used in TLS 1.3.
hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,  # We want a 256-bit (32-byte) key for AES
    salt=None,
    info=b"handshake_data",
)
session_key = hkdf.derive(shared_secret)
print(f"Session key derived from shared secret: {session_key.hex()}")

# Step D: Encrypted Communication with the Session Key

# 1. Client encrypts a message with the session key using AES-GCM
nonce = os.urandom(12)  # GCM requires a nonce
cipher = Cipher(algorithms.AES(session_key), modes.GCM(nonce))
encryptor = cipher.encryptor()

plaintext = b"This is a top secret message from the client!"
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
auth_tag = encryptor.tag  # GCM provides an authentication tag

print(f"\nClient sends encrypted message: {ciphertext.hex()}")

# 2. Server decrypts the message
# The server would have derived the same session key
decryptor_cipher = Cipher(algorithms.AES(session_key), modes.GCM(nonce, auth_tag))
decryptor = decryptor_cipher.decryptor()
decrypted_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print(f"Server decrypts message: {decrypted_plaintext.decode()}")

assert plaintext == decrypted_plaintext
print(
    "\nSuccess! The simulated TLS session successfully exchanged an encrypted message."
)
