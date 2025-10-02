from math import gcd

# Step 1 - define p and q
p = 3
q = 7

# Step 2 - calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)


# Step 3 - choose an integer e (public exponent) such that 1 < e < phi(n) and gcd(e, phi_n) == 1
def find_e(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e
    return None


e = find_e(phi_n)


# Step 4 - calculate d (private exponent) such that (d * e) % phi_n == 1
def mod_inverse(e, phi_n):
    # Extended Euclidean Algorithm
    t1, t2 = 0, 1
    r1, r2 = phi_n, e

    while r2 > 0:
        quotient = r1 // r2
        r1, r2 = r2, r1 - quotient * r2
        t1, t2 = t2, t1 - quotient * t2

    if r1 == 1:
        return t1 % phi_n
    else:
        return None


d = mod_inverse(e, phi_n)


# Step 5: RSA Encryption
def encrypt(message, e, n):
    return pow(message, e, n)


# Step 6: RSA Decryption
def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)


# Example usage:
message = 5  # message must be less than nc (n = 21)
ciphertext = encrypt(message, e, n)
decrypted_message = decrypt(ciphertext, d, n)

# Output public and private keys
print(f"Public Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")
print(f"Original Message: {message}")
print(f"Encrypted Message: {ciphertext}")
print(f"Dencrypted Message: {decrypted_message}")
