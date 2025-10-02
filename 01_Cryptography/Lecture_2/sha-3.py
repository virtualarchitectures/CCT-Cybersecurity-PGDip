import hashlib

# Example message
message = "Hello, World!"

# Create a new SHA3-256 hash object
sha3_256_hash = hashlib.sha3_256()

# Update the hash object with the message (encoded to bytes)
sha3_256_hash.update(message.encode("utf-8"))

# Get the hexidecimal digest (hash value)  of the message
hash_value = sha3_256_hash.hexdigest()

# Output the SHA-256 hash
print(f"SHA-256 Hash of {message}: {hash_value}")
