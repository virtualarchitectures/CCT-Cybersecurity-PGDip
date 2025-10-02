def is_even(number):
    """
    Checks if an integer is even.

    Args:
        number: An integer (positive, negative, or zero).

    Returns:
        True if the number is even, False otherwise.
    """
    return number % 2 == 0

def print_even_odd(number):
    """
    Prints "Even" if the input number is even, and "Odd" otherwise.

    This function uses the `is_even` function to determine evenness.

    Args:
        number: An integer (positive, negative, or zero).

    Returns:
        None (This function prints to the console, it doesn't return a value).

    Example:
        print_even_odd(4)  # Prints "Even"
        print_even_odd(7)  # Prints "Odd"
        print_even_odd(-2) # Prints "Even"
        print_even_odd(0)  # Prints "Even"
    """
    # Call the is_even function to check if the number is even.
    if is_even(number):
        # If is_even returns True, print "Even".
        print("Even")
    else:
        # Otherwise (if is_even returns False), print "Odd".
        print("Odd")

# --- Test Cases ---
test_cases = [
    2,      # Even positive
    4,      # Even positive
    0,      # Zero (even)
    -2,     # Even negative
    -4,     # Even negative
    1,      # Odd positive
    3,      # Odd positive
    -1,     # Odd negative
    -3,     # Odd negative
    15,    # odd positive
    22   #even positive
]

# This loop goes through each test case and calls print_even_odd.
for num in test_cases:
    print(f"Input: {num}, ", end="")  # Print the input number. end="" prevents a newline.
    print_even_odd(num)  # Call the function to print "Even" or "Odd".