# Character set
CHARSET = list("abcdefghijklmnopqrstuvwxyz")


def encrypt(text, shift):
    # Convert input to lowercase and remove non-alpha characters
    cleaned_text = "".join(char.lower() for char in text if char.isalpha())
    result = ""

    for char in cleaned_text:
        # Find the current position in the charset
        current_pos = CHARSET.index(char)
        # Calculate new position with shift
        new_pos = (current_pos + shift) % len(CHARSET)
        # Add the shifted character to result
        result += CHARSET[new_pos]

    print("Encrypted ciphertext: " + result)
    return result


def decrypt(text, shift):
    # Convert input to lowercase and remove non-alpha characters
    cleaned_text = "".join(char.lower() for char in text if char.isalpha())
    result = ""

    for char in cleaned_text:
        # Find the current position in the charset
        current_pos = CHARSET.index(char)
        # Calculate new position reversing the shift
        new_pos = (current_pos - shift) % len(CHARSET)
        # Add the shifted character to result
        result += CHARSET[new_pos]

    print("Decrypted message: " + result)
    return result


if __name__ == "__main__":
    message = "Hello, World!"
    key = 3

    print(f"Original message: {message}")

    # Test the encryption and decryption
    encrypted = encrypt(text=message, shift=key)
    decrypted = decrypt(text=encrypted, shift=key)
