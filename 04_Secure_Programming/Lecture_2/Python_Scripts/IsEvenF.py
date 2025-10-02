def is_even(number):
    """
    Checks if an integer is even.

    Args:
        number: An integer (positive, negative, or zero).

    Returns:
        True if the number is even, False otherwise.

    Example:
        is_even(4)  # Returns True
        is_even(7)  # Returns False
        is_even(-2) # Returns True
        is_even(0)  # Returns True
    """
    # The modulo operator (%) gives the remainder of a division.
    # If a number is perfectly divisible by 2 (i.e., it's even),
    # the remainder will be 0.  So, we check if the remainder is 0.
    return number % 2 == 0


# --- Test Cases ---
# These examples test the function with various inputs to make
# sure it works correctly in all cases.
test_cases = [
    (2, True),      # Even positive number
    (4, True),      # Another even positive number
    (0, True),      # Zero is considered an even number
    (-2, True),     # Even negative number
    (-4, True),     # Another even negative number
    (1, False),     # Odd positive number
    (3, False),     # Another odd positive number
    (-1, False),    # Odd negative number
    (-3, False),    # Another odd negative number
]

# This loop goes through each test case.
for num, expected in test_cases:
    # Call the 'is_even' function with the current number.
    result = is_even(num)
    # Print a message showing the input, the result, the expected result,
    # and whether the test passed (the result matches the expected value).
    print(f"Input: {num}, Output: {result}, Expected: {expected}, Pass: {result == expected}")


# --- Alternative Implementation using Bitwise AND (More Advanced) ---
# This is a faster way to check for evenness, but it's a bit more
# advanced, so it's explained separately.

def is_even_bitwise(number):
    """
    Checks if an integer is even using a bitwise AND operation.

    Args:
        number: An integer.

    Returns:
        True if the number is even, False otherwise.

    Explanation:
        In binary representation, even numbers always have a 0 in their
        least significant bit (LSB - the rightmost bit). Odd numbers
        have a 1 in their LSB.

        The bitwise AND operator (&) compares the bits of two numbers.
        If both bits are 1, the result is 1.  Otherwise, the result is 0.

        When we do 'number & 1', we are essentially isolating the LSB:
          - If the LSB of 'number' is 1, the result of 'number & 1' is 1.
          - If the LSB of 'number' is 0, the result of 'number & 1' is 0.

        Therefore, '(number & 1) == 0' is True only if the LSB is 0
        (meaning the number is even).

    Example (Binary):
        5 (decimal) = 0101 (binary)
        1 (decimal) = 0001 (binary)
        5 & 1       = 0001 (binary) = 1 (decimal)  -> Odd

        4 (decimal) = 0100 (binary)
        1 (decimal) = 0001 (binary)
        4 & 1       = 0000 (binary) = 0 (decimal)  -> Even
    """
    # Use the bitwise AND operator (&) with 1 to check the least
    # significant bit.  If it's 0, the number is even.
    return (number & 1) == 0

# Test cases for bitwise version (same test cases as before).
for num, expected in test_cases:
    result = is_even_bitwise(num)
    print(f"Input: {num}, Output: {result}, Expected: {expected}, Pass: {result == expected}")