# This program converts Celsius to Fahrenheit.

# Prompt the user to enter a temperature in Celsius.
celsius_str = input("Enter the temperature in Celsius: ")

# Convert the input string to a floating-point number.
# Use float() to allow for decimal values.
celsius = float(celsius_str)

# Apply the conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Display the converted temperature in Fahrenheit.
# Use an f-string to embed the celsius and fahrenheit values.
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Example of rounding the result to two decimal places.
rounded_fahrenheit = round(fahrenheit, 2)
print(f"{celsius} degrees Celsius is equal to {rounded_fahrenheit} degrees Fahrenheit (rounded).")