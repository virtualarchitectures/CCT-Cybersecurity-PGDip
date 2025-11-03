# AES Implementation
# Your Name: Oliver Dawkins


def text_to_hex_matrix(plaintext):
    """Convert 16-character string to 4x4 hex matrix (column-major)"""
    # Create empty 4x4 matrix
    matrix = [[0 for _ in range(4)] for _ in range(4)]

    # Fill matrix in column-major order
    for i, char in enumerate(plaintext):
        # For column-major: row = i % 4, col = i // 4
        row = i % 4
        col = i // 4
        # Use ord(char) to get the character's ASCII value
        matrix[row][col] = ord(char)

    return matrix


def hex_matrix_to_text(matrix):
    """Convert a 4x4 hex matrix back to a 16-character string"""
    plaintext = ""
    # Iterate columns first for column-major order
    for col in range(4):
        for row in range(4):
            plaintext += chr(matrix[row][col])
    return plaintext


def sub_bytes(state_matrix):
    """Apply S-box substitution to each byte in the matrix"""

    S_BOX = [
        [
            0x63,
            0x7C,
            0x77,
            0x7B,
            0xF2,
            0x6B,
            0x6F,
            0xC5,
            0x30,
            0x01,
            0x67,
            0x2B,
            0xFE,
            0xD7,
            0xAB,
            0x76,
        ],
        [
            0xCA,
            0x82,
            0xC9,
            0x7D,
            0xFA,
            0x59,
            0x47,
            0xF0,
            0xAD,
            0xD4,
            0xA2,
            0xAF,
            0x9C,
            0xA4,
            0x72,
            0xC0,
        ],
        [
            0xB7,
            0xFD,
            0x93,
            0x26,
            0x36,
            0x3F,
            0xF7,
            0xCC,
            0x34,
            0xA5,
            0xE5,
            0xF1,
            0x71,
            0xD8,
            0x31,
            0x15,
        ],
        [
            0x04,
            0xC7,
            0x23,
            0xC3,
            0x18,
            0x96,
            0x05,
            0x9A,
            0x07,
            0x12,
            0x80,
            0xE2,
            0xEB,
            0x27,
            0xB2,
            0x75,
        ],
        [
            0x09,
            0x83,
            0x2C,
            0x1A,
            0x1B,
            0x6E,
            0x5A,
            0xA0,
            0x52,
            0x3B,
            0xD6,
            0xB3,
            0x29,
            0xE3,
            0x2F,
            0x84,
        ],
        [
            0x53,
            0xD1,
            0x00,
            0xED,
            0x20,
            0xFC,
            0xB1,
            0x5B,
            0x6A,
            0xCB,
            0xBE,
            0x39,
            0x4A,
            0x4C,
            0x58,
            0xCF,
        ],
        [
            0xD0,
            0xEF,
            0xAA,
            0xFB,
            0x43,
            0x4D,
            0x33,
            0x85,
            0x45,
            0xF9,
            0x02,
            0x7F,
            0x50,
            0x3C,
            0x9F,
            0xA8,
        ],
        [
            0x51,
            0xA3,
            0x40,
            0x8F,
            0x92,
            0x9D,
            0x38,
            0xF5,
            0xBC,
            0xB6,
            0xDA,
            0x21,
            0x10,
            0xFF,
            0xF3,
            0xD2,
        ],
        [
            0xCD,
            0x0C,
            0x13,
            0xEC,
            0x5F,
            0x97,
            0x44,
            0x17,
            0xC4,
            0xA7,
            0x7E,
            0x3D,
            0x64,
            0x5D,
            0x19,
            0x73,
        ],
        [
            0x60,
            0x81,
            0x4F,
            0xDC,
            0x22,
            0x2A,
            0x90,
            0x88,
            0x46,
            0xEE,
            0xB8,
            0x14,
            0xDE,
            0x5E,
            0x0B,
            0xDB,
        ],
        [
            0xE0,
            0x32,
            0x3A,
            0x0A,
            0x49,
            0x06,
            0x24,
            0x5C,
            0xC2,
            0xD3,
            0xAC,
            0x62,
            0x91,
            0x95,
            0xE4,
            0x79,
        ],
        [
            0xE7,
            0xC8,
            0x37,
            0x6D,
            0x8D,
            0xD5,
            0x4E,
            0xA9,
            0x6C,
            0x56,
            0xF4,
            0xEA,
            0x65,
            0x7A,
            0xAE,
            0x08,
        ],
        [
            0xBA,
            0x78,
            0x25,
            0x2E,
            0x1C,
            0xA6,
            0xB4,
            0xC6,
            0xE8,
            0xDD,
            0x74,
            0x1F,
            0x4B,
            0xBD,
            0x8B,
            0x8A,
        ],
        [
            0x70,
            0x3E,
            0xB5,
            0x66,
            0x48,
            0x03,
            0xF6,
            0x0E,
            0x61,
            0x35,
            0x57,
            0xB9,
            0x86,
            0xC1,
            0x1D,
            0x9E,
        ],
        [
            0xE1,
            0xF8,
            0x98,
            0x11,
            0x69,
            0xD9,
            0x8E,
            0x94,
            0x9B,
            0x1E,
            0x87,
            0xE9,
            0xCE,
            0x55,
            0x28,
            0xDF,
        ],
        [
            0x8C,
            0xA1,
            0x89,
            0x0D,
            0xBF,
            0xE6,
            0x42,
            0x68,
            0x41,
            0x99,
            0x2D,
            0x0F,
            0xB0,
            0x54,
            0xBB,
            0x16,
        ],
    ]

    # Create a new empty 4x4 matrix
    matrix = [[0 for _ in range(4)] for _ in range(4)]

    # For each byte in the 4x4 matrix, use its value to look up the S-box
    for row in range(4):
        for col in range(4):
            # Retrieve the current byte from the state matrix
            byte = state_matrix[row][col]
            # High 4 bits = row, low 4 bits = column
            # Use `byte >> 4` for row and `byte & 0x0F` for column.
            s_row = (byte >> 4) & 0x0F
            s_col = byte & 0x0F
            # Replace the byte with the S-box value
            matrix[row][col] = S_BOX[s_row][s_col]

    return matrix


def inverse_sub_bytes(state_matrix):
    """Apply inverse S-box substitution to each byte in the matrix"""

    INV_S_BOX = [
        [
            0x52,
            0x09,
            0x6A,
            0xD5,
            0x30,
            0x36,
            0xA5,
            0x38,
            0xBF,
            0x40,
            0xA3,
            0x9E,
            0x81,
            0xF3,
            0xD7,
            0xFB,
        ],
        [
            0x7C,
            0xE3,
            0x39,
            0x82,
            0x9B,
            0x2F,
            0xFF,
            0x87,
            0x34,
            0x8E,
            0x43,
            0x44,
            0xC4,
            0xDE,
            0xE9,
            0xCB,
        ],
        [
            0x54,
            0x7B,
            0x94,
            0x32,
            0xA6,
            0xC2,
            0x23,
            0x3D,
            0xEE,
            0x4C,
            0x95,
            0x0B,
            0x42,
            0xFA,
            0xC3,
            0x4E,
        ],
        [
            0x08,
            0x2E,
            0xA1,
            0x66,
            0x28,
            0xD9,
            0x24,
            0xB2,
            0x76,
            0x5B,
            0xA2,
            0x49,
            0x6D,
            0x8B,
            0xD1,
            0x25,
        ],
        [
            0x72,
            0xF8,
            0xF6,
            0x64,
            0x86,
            0x68,
            0x98,
            0x16,
            0xD4,
            0xA4,
            0x5C,
            0xCC,
            0x5D,
            0x65,
            0xB6,
            0x92,
        ],
        [
            0x6C,
            0x70,
            0x48,
            0x50,
            0xFD,
            0xED,
            0xB9,
            0xDA,
            0x5E,
            0x15,
            0x46,
            0x57,
            0xA7,
            0x8D,
            0x9D,
            0x84,
        ],
        [
            0x90,
            0xD8,
            0xAB,
            0x00,
            0x8C,
            0xBC,
            0xD3,
            0x0A,
            0xF7,
            0xE4,
            0x58,
            0x05,
            0xB8,
            0xB3,
            0x45,
            0x06,
        ],
        [
            0xD0,
            0x2C,
            0x1E,
            0x8F,
            0xCA,
            0x3F,
            0x0F,
            0x02,
            0xC1,
            0xAF,
            0xBD,
            0x03,
            0x01,
            0x13,
            0x8A,
            0x6B,
        ],
        [
            0x3A,
            0x91,
            0x11,
            0x41,
            0x4F,
            0x67,
            0xDC,
            0xEA,
            0x97,
            0xF2,
            0xCF,
            0xCE,
            0xF0,
            0xB4,
            0xE6,
            0x73,
        ],
        [
            0x96,
            0xAC,
            0x74,
            0x22,
            0xE7,
            0xAD,
            0x35,
            0x85,
            0xE2,
            0xF9,
            0x37,
            0xE8,
            0x1C,
            0x75,
            0xDF,
            0x6E,
        ],
        [
            0x47,
            0xF1,
            0x1A,
            0x71,
            0x1D,
            0x29,
            0xC5,
            0x89,
            0x6F,
            0xB7,
            0x62,
            0x0E,
            0xAA,
            0x18,
            0xBE,
            0x1B,
        ],
        [
            0xFC,
            0x56,
            0x3E,
            0x4B,
            0xC6,
            0xD2,
            0x79,
            0x20,
            0x9A,
            0xDB,
            0xC0,
            0xFE,
            0x78,
            0xCD,
            0x5A,
            0xF4,
        ],
        [
            0x1F,
            0xDD,
            0xA8,
            0x33,
            0x88,
            0x07,
            0xC7,
            0x31,
            0xB1,
            0x12,
            0x10,
            0x59,
            0x27,
            0x80,
            0xEC,
            0x5F,
        ],
        [
            0x60,
            0x51,
            0x7F,
            0xA9,
            0x19,
            0xB5,
            0x4A,
            0x0D,
            0x2D,
            0xE5,
            0x7A,
            0x9F,
            0x93,
            0xC9,
            0x9C,
            0xEF,
        ],
        [
            0xA0,
            0xE0,
            0x3B,
            0x4D,
            0xAE,
            0x2A,
            0xF5,
            0xB0,
            0xC8,
            0xEB,
            0xBB,
            0x3C,
            0x83,
            0x53,
            0x99,
            0x61,
        ],
        [
            0x17,
            0x2B,
            0x04,
            0x7E,
            0xBA,
            0x77,
            0xD6,
            0x26,
            0xE1,
            0x69,
            0x14,
            0x63,
            0x55,
            0x21,
            0x0C,
            0x7D,
        ],
    ]

    # Create a new empty 4x4 matrix
    matrix = [[0 for _ in range(4)] for _ in range(4)]

    # For each byte in the 4x4 matrix, use its value to look up the inverse S-box
    for row in range(4):
        for col in range(4):
            # Retrieve the current byte from the state matrix
            byte = state_matrix[row][col]
            # High 4 bits = row, low 4 bits = column
            # Use `byte >> 4` for row and `byte & 0x0F` for column.
            s_row = (byte >> 4) & 0x0F
            s_col = byte & 0x0F
            # Replace the byte with the inverse S-box value
            matrix[row][col] = INV_S_BOX[s_row][s_col]

    return matrix


def shift_rows(state_matrix):
    """Perform row shifts on the state matrix"""

    # Create a new empty 4x4 matrix
    matrix = [[0 for _ in range(4)] for _ in range(4)]

    # Loop over each byte in the 4x4 matrix and shift value by row
    for row in range(4):
        for col in range(4):
            # Shift left by 'row' positions
            # Row 0: No shift
            # Row 1: Left shift by 1 position
            # Row 2: Left shift by 2 positions
            # Row 3: Left shift by 3 positions
            # Set the new column position for each byte after the shift
            new_col = (col - row) % 4
            # Assign the left shifted value to the new column position
            matrix[row][new_col] = state_matrix[row][col]

    return matrix


def inverse_shift_rows(state_matrix):
    """Perform inverse row shifts on the state matrix"""
    new_matrix = [[0 for _ in range(4)] for _ in range(4)]

    # Loop over each byte in the 4x4 matrix and shift value by row
    for row in range(4):
        for col in range(4):
            # Shift right by 'row' positions
            # Row 0: No shift
            # Row 1: Right shift by 1 position
            # Row 2: Right shift by 2 positions
            # Row 3: Right shift by 3 positions
            # Set the new column position for each byte after the shift
            new_col = (col + row) % 4
            # Assign the left shifted value to the new column position
            new_matrix[row][new_col] = state_matrix[row][col]

    return new_matrix


def add_round_key(state_matrix, round_key):
    """XOR state matrix with round key"""

    # Create a new empty 4x4 matrix
    matrix = [[0 for _ in range(4)] for _ in range(4)]

    # Loop over each byte in the 4x4 matrix
    for row in range(4):
        for col in range(4):
            # XOR each byte with the corresponding byte of the round key
            # Use the `^` operator for XOR
            matrix[row][col] = state_matrix[row][col] ^ round_key[row][col]

    return matrix


def print_matrix(matrix, title="Matrix"):
    """Pretty print a matrix in hexadecimal format"""
    print(f"\n{title}:")
    for row in matrix:
        print([f"{byte:02x}" for byte in row])


def aes_encryption(plaintext, main_key, num_rounds=10):
    """Perform complete AES encryption with multiple rounds"""
    print(f"\nPlaintext Input: '{plaintext}'")

    state = text_to_hex_matrix(plaintext)
    print_matrix(state, "Initial State")

    # Initial AddRoundKey
    state = add_round_key(state, main_key)
    print_matrix(state, "After Initial AddRoundKey")

    # Main AES Rounds
    for round in range(1, num_rounds + 1):
        print(f"\n== Round {round} ==")

        # Generate or retrieve proper round key for each round (using main_key here)
        round_key = (
            main_key  # Replace with the appropriate key schedule logic for real use
        )

        # Apply SubBytes
        state = sub_bytes(state)
        print_matrix(state, "After SubBytes")

        # Apply ShiftRows
        state = shift_rows(state)
        print_matrix(state, "After ShiftRows")

        # NOTE: MixColumns is omitted in the final round of standard AES

        # Apply AddRoundKey
        state = add_round_key(state, round_key)
        print_matrix(state, "After AddRoundKey")

    # Display the encrypted matrix
    print("\n=== Encrypted Result ===")
    print_matrix(state, "Encrypted State Matrix")
    # Convert the state matrix to text
    ciphertext = hex_matrix_to_text(state)

    return ciphertext


def aes_decryption(ciphertext, main_key, num_rounds=10):
    """Perform complete AES decryption with multiple rounds"""
    print(f"\nCiphertext Input: '{ciphertext}'")

    # Convert the ciphertext to a matrix
    ciphertext_matrix = text_to_hex_matrix(ciphertext)

    state = ciphertext_matrix
    print_matrix(state, "Initial Ciphertext Matrix")

    # Initial AddRoundKey with the final round key
    state = add_round_key(state, main_key)
    print_matrix(state, "After Initial AddRoundKey")

    # Main AES Rounds (in reverse order)
    for round in range(num_rounds, 0, -1):
        print(f"\n== Round {round} ==")

        # Generate or retrieve proper round key for each round (using main_key here)
        round_key = (
            main_key  # Replace with the appropriate key schedule logic for real use
        )

        # Apply Inverse ShiftRows
        state = inverse_shift_rows(state)
        print_matrix(state, "After Inverse ShiftRows")

        # Apply Inverse SubBytes
        state = inverse_sub_bytes(state)
        print_matrix(state, "After Inverse SubBytes")

        # Apply AddRoundKey
        state = add_round_key(state, round_key)
        print_matrix(state, "After AddRoundKey")

    # Display the decrypted result
    print("\n=== Decrypted Result ===")
    print_matrix(state, "Decrypted State Matrix")
    # Convert the state matrix to text
    plaintext = hex_matrix_to_text(state)

    return plaintext


if __name__ == "__main__":

    # plaintext = "HELLO WORLD!!!!!"  # Exactly 16 characters
    plaintext = "ABCDEFGHIJKLMNOP"

    round_key = [
        [0x2B, 0x28, 0xAB, 0x09],
        [0x7E, 0xAE, 0xF7, 0xCF],
        [0x15, 0xD2, 0x15, 0x4F],
        [0x16, 0xA6, 0x88, 0x3C],
    ]

    num_rounds = 10

    print("=== AES Encryption ===")
    ciphertext = aes_encryption(plaintext, round_key, num_rounds)
    print(f"\nCiphertext: '{ciphertext}'")

    print("=== AES Decryption ===")
    decrypted_plaintext = aes_decryption(ciphertext, round_key, num_rounds)
    print(f"\nDecrypted plaintext: {decrypted_plaintext}")
