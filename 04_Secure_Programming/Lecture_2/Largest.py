# This program finds the largest of three numbers.

# Prompt the user to enter the first number.
num1_str = input("Enter the first number: ")

# Prompt the user to enter the second number.
num2_str = input("Enter the second number: ")

# Prompt the user to enter the third number.
num3_str = input("Enter the third number: ")

# Convert the input strings to floating-point numbers.
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
    num3 = float(num3_str)

    # Use conditional statements to find the largest number.
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    # Print the largest number.
    print(f"The largest number is: {largest}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")

# Alternative method using the built-in max() function.
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
    num3 = float(num3_str)

    largest_max = max(num1, num2, num3)
    print(f"The largest number (using max()) is: {largest_max}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")