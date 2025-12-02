# ==============================================================================
# Part 1: Setup
# Install the required libraries.
# 'cryptography' is a standard library for classical crypto.
# 'kyber' is a pure Python implementation of the CRYSTALS-Kyber PQC algorithm.
# ==============================================================================

# Import necessary modules
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from kyber_py.kyber import Kyber512  # For CRYSTALS-Kyber

# ==============================================================================
#
# LECTURE DEMONSTRATION SCRIPT
# Title: Comparing Classical vs. Post-Quantum Key Exchange
#
# Objective: To tangibly demonstrate the size difference between keys in
#            a classical algorithm (ECDH) and a post-quantum algorithm (Kyber).
#
# ==============================================================================

print("=" * 80)
print(" CRYPTOGRAPHY LECTURE: PRACTICAL DEMONSTRATION")
print("=" * 80)
print(
    "\nWelcome! This script will demonstrate the key generation and encapsulation process for:"
)
print("  1. A classical, widely-used algorithm: Elliptic Curve Diffie-Hellman (ECDH)")
print("  2. A new, NIST-standardized post-quantum algorithm: CRYSTALS-Kyber\n")
print(
    "Our goal is to observe the practical differences, especially in the size of the keys.\n"
)


# ==============================================================================
# Step 1: Classical Key Exchange with Elliptic Curve Diffie-Hellman (ECDH)
# ==============================================================================

print("--- [PART 1: CLASSICAL KEY EXCHANGE (ECDH)] ---")

# We'll use the SECP256R1 curve, which is a common standard (e.g., for TLS).
# It offers a security level roughly equivalent to a 128-bit symmetric key.

# 1.1: Alice generates her key pair.
print("\n1.1: Alice is generating her classical ECDH key pair...")
alice_private_key_ecdh = ec.generate_private_key(ec.SECP256R1())
alice_public_key_ecdh = alice_private_key_ecdh.public_key()

# Serialize the public key to get its byte representation for transmission.
# We use the common uncompressed format.
alice_public_key_bytes_ecdh = alice_public_key_ecdh.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint,
)

print(f"  -> Alice's Public Key Size: {len(alice_public_key_bytes_ecdh)} bytes")
print("     (This is the data Alice would send to Bob over the network.)")


# 1.2: Bob does the same.
print("\n1.2: Bob is generating his classical ECDH key pair...")
bob_private_key_ecdh = ec.generate_private_key(ec.SECP256R1())
bob_public_key_ecdh = bob_private_key_ecdh.public_key()
bob_public_key_bytes_ecdh = bob_public_key_ecdh.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint,
)
print(f"  -> Bob's Public Key Size: {len(bob_public_key_bytes_ecdh)} bytes")


# 1.3: Alice and Bob exchange keys and derive a shared secret.
print("\n1.3: Alice and Bob exchange public keys and derive a shared secret.")
shared_secret_alice = alice_private_key_ecdh.exchange(ec.ECDH(), bob_public_key_ecdh)
shared_secret_bob = bob_private_key_ecdh.exchange(ec.ECDH(), alice_public_key_ecdh)

# Check if the secrets match.
assert shared_secret_alice == shared_secret_bob
print(f"  -> Shared secret successfully derived by both parties.")
print(f"  -> Length of the shared secret: {len(shared_secret_alice)} bytes (256 bits)")


# ==============================================================================
# Step 2: Post-Quantum Key Encapsulation Mechanism (KEM) with CRYSTALS-Kyber
# ==============================================================================

print("\n\n--- [PART 2: POST-QUANTUM KEY ENCAPSULATION (Kyber)] ---")

# We will use Kyber-512, the smallest parameter set for Kyber, which aims for a
# security level comparable to AES-128 (and our ECDH example).

# In a KEM, the process is slightly different from a key exchange:
# 1. The receiver (Bob) generates a key pair and sends his public key to the sender (Alice).
# 2. The sender (Alice) uses the public key to generate a shared secret AND "encapsulates"
#    it into a ciphertext. She sends this ciphertext to the receiver.
# 3. The receiver (Bob) uses his private key to "decapsulate" the ciphertext and retrieve
#    the exact same shared secret.

# 2.1: Bob (the receiver) generates his Kyber key pair.
print("\n2.1: Bob is generating his post-quantum Kyber key pair...")
bob_public_key_kyber, bob_private_key_kyber = Kyber512.keygen()

print(f"  -> Bob's Public Key Size: {len(bob_public_key_kyber)} bytes")
print(
    "     (This is what Bob would send to Alice. Notice the size difference already!)"
)


# 2.2: Alice (the sender) receives Bob's public key and generates a shared secret.
print("\n2.2: Alice receives Bob's public key and uses it to generate a shared secret.")
# Alice creates the shared secret and the ciphertext to send back to Bob.
shared_secret_alice_kyber, ciphertext_kyber = Kyber512.encaps(bob_public_key_kyber)

print(
    f"  -> Alice generated a shared secret of {len(shared_secret_alice_kyber)} bytes."
)
print(
    f"  -> To send it, she created a 'ciphertext' of size: {len(ciphertext_kyber)} bytes"
)
print("     (This ciphertext is what Alice sends to Bob.)")


# 2.3: Bob receives the ciphertext and uses his private key to get the secret.
print("\n2.3: Bob receives the ciphertext and uses his private key to decapsulate it.")
shared_secret_bob_kyber = Kyber512.decaps(bob_private_key_kyber, ciphertext_kyber)

print(f"  -> Bob recovered the shared secret.")

# Check if the secrets match.
assert shared_secret_alice_kyber == shared_secret_bob_kyber
print(f"  -> Shared secret successfully established by both parties.")
print(
    f"  -> Length of the shared secret: {len(shared_secret_bob_kyber)} bytes (256 bits)"
)


# ==============================================================================
# Step 3: Final Comparison and Conclusion
# ==============================================================================

print("\n\n" + "=" * 80)
print(" FINAL COMPARISON: ECDH (SECP256R1) vs. Kyber (Kyber-512)")
print("=" * 80)

print(f"\nSecurity Level: Both aim for security comparable to AES-128.")
print(f"Quantum Vulnerability: ECDH is BROKEN by quantum computers. Kyber is NOT.")

print("\n--- Data Size Comparison ---")
print(f"Public Key Size (the main overhead for transmission):")
print(f"  -> Classical ECDH: {len(alice_public_key_bytes_ecdh):>5} bytes")
print(f"  -> Post-Quantum Kyber: {len(bob_public_key_kyber):>5} bytes")

print(f"\nCiphertext Size (for sending the secret):")
print(f"  -> Classical ECDH: N/A (key is derived, not encapsulated)")
print(f"  -> Post-Quantum Kyber: {len(ciphertext_kyber):>5} bytes")

factor = len(bob_public_key_kyber) / len(alice_public_key_bytes_ecdh)
print(
    f"\nConclusion: The Kyber public key is {factor:.1f} times larger than the ECDH public key."
)
print("This is the practical trade-off for achieving quantum resistance.")
print("Engineers must account for this increased data size when upgrading systems,")
print("especially in bandwidth-constrained environments like IoT.")
print("\n" + "=" * 80)
print(" END OF DEMONSTRATION")
print("=" * 80)
