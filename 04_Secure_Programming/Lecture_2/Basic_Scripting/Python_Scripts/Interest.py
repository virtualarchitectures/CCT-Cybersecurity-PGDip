# This program calculates simple interest.

# Prompt the user to enter the principal amount.
principal_str = input("Enter the principal amount: ")

# Convert the input string to a floating-point number.
principal = float(principal_str)

# Prompt the user to enter the annual interest rate.
rate_str = input("Enter the annual interest rate (in percentage): ")

# Convert the input string to a floating-point number.
rate = float(rate_str)

# Prompt the user to enter the time period in years.
time_str = input("Enter the time period in years: ")

# Convert the input string to a floating-point number.
time = float(time_str)

# Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100
simple_interest = (principal * rate * time) / 100

# Display the calculated simple interest.
# Use an f-string to embed the calculated interest value.
print(f"The simple interest is: {simple_interest}")

# Example of rounding the result to two decimal places.
rounded_interest = round(simple_interest, 2)
print(f"The simple interest (rounded) is: {rounded_interest}")