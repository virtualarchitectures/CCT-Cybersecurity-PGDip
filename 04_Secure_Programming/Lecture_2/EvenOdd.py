# This program checks if an integer is even or odd.

# Prompt the user to enter an integer.
input_str = input("Enter an integer: ")

# Convert the input string to an integer.
try:
    number = int(input_str)

    # Check if the number is even or odd using the modulo operator (%).
    # If the remainder when divided by 2 is 0, the number is even.
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")