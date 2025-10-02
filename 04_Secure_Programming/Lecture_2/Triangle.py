# This program calculates the area of a triangle.

# Prompt the user to enter the base of the triangle.
base_str = input("Enter the base of the triangle: ")

# Convert the input string to a floating-point number.
# Use float() to allow for decimal values.
base = float(base_str)

# Prompt the user to enter the height of the triangle.
height_str = input("Enter the height of the triangle: ")

# Convert the input string to a floating-point number.
height = float(height_str)

# Calculate the area of the triangle using the formula: area = (1/2) * base * height
area = 0.5 * base * height

# Display the calculated area to the user.
# Use an f-string to embed the area value directly into the output string.
print(f"The area of the triangle is: {area}")

#Example of how to round the output to two decimal places.
rounded_area = round(area, 2)
print(f"The rounded area of the triangle is: {rounded_area}")