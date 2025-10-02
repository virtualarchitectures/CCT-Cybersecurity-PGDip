# Function to calculate the power of a number.
def power(base, exponent=2):
    """
    This function calculates the power of a base raised to an exponent.

    Args:
        base (int): The base number.
        exponent (int, optional): The exponent. Defaults to 2.

    Returns:
        int: The result of base raised to the power of exponent.
    """
    result = base ** exponent
    return result

# Call the power function with different base values, both with and without providing the exponent argument.
result1 = power(5)  # Using the default exponent (2).
print(f"5 to the power of 2: {result1}")

result2 = power(3, 3)  # Providing a custom exponent (3).
print(f"3 to the power of 3: {result2}")

result3 = power(10) # Using the default exponent (2).
print(f"10 to the power of 2: {result3}")

result4 = power(2, 8) # Providing a custom exponent (8).
print(f"2 to the power of 8: {result4}")

result5 = power(-2) # Using the default exponent (2).
print(f"-2 to the power of 2: {result5}")