# Character set (same as caesar_cipher)
CHARSET = list("abcdefghijklmnopqrstuvwxyz")

def prepare_key(key, text_length):
    """
    Prepare the key by repeating it to match the length of the text
    """
    # Convert key to lowercase and remove non-alpha characters
    cleaned_key = "".join(char.lower() for char in key if char.isalpha())
    # Repeat the key to match or exceed text length, then trim to exact length
    return (cleaned_key * (text_length // len(cleaned_key) + 1))[:text_length]

def encrypt(text, key):
    # Convert input to lowercase and remove non-alpha characters
    cleaned_text = "".join(char.lower() for char in text if char.isalpha())
    # Prepare the key to match the text length
    full_key = prepare_key(key, len(cleaned_text))
    result = ""

    for i, char in enumerate(cleaned_text):
        # Find the current position of the text character
        text_pos = CHARSET.index(char)
        # Find the shift value from the key character
        key_pos = CHARSET.index(full_key[i])
        # Calculate new position with the key-based shift
        new_pos = (text_pos + key_pos) % len(CHARSET)
        # Add the shifted character to result
        result += CHARSET[new_pos]

    print("Encrypted ciphertext: " + result)
    return result

def decrypt(text, key):
    # Convert input to lowercase and remove non-alpha characters
    cleaned_text = "".join(char.lower() for char in text if char.isalpha())
    # Prepare the key to match the text length
    full_key = prepare_key(key, len(cleaned_text))
    result = ""

    for i, char in enumerate(cleaned_text):
        # Find the current position of the cipher character
        text_pos = CHARSET.index(char)
        # Find the shift value from the key character
        key_pos = CHARSET.index(full_key[i])
        # Calculate new position by reversing the key-based shift
        new_pos = (text_pos - key_pos) % len(CHARSET)
        # Add the unshifted character to result
        result += CHARSET[new_pos]

    print("Decrypted message: " + result)
    return result

if __name__ == "__main__":
    message = "Hello, World!"
    key = "SECRET"  # The keyword for Vigenère cipher

    print(f"Original message: {message}")
    print(f"Using key: {key}")

    # Test the encryption and decryption
    encrypted = encrypt(text=message, key=key)
    decrypted = decrypt(text=encrypted, key=key)
