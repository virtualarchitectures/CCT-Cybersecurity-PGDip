# This program checks if a year is a leap year.

# Prompt the user to enter a year.
year_str = input("Enter a year: ")

# Convert the input string to an integer.
try:
    year = int(year_str)

    # Check if the year is a leap year using the leap year rules.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

except ValueError:
    print("Invalid input. Please enter a valid year (an integer).")