# This program reverses a string.

# Prompt the user to enter a string.
input_string = input("Enter a string: ")

# Reverse the string using string slicing.
# [::-1] creates a reversed copy of the string.
reversed_string = input_string[::-1]

# Print the reversed string.
print("Reversed string:", reversed_string)

#Alternative method using a loop.
# Initialize an empty string to store the reversed string.
reversed_string_loop = ""

# Iterate through the input string from the end to the beginning.
for i in range(len(input_string) - 1, -1, -1):
    # Append each character to the reversed string.
    reversed_string_loop += input_string[i]

# Print the reversed string created by the loop.
print("Reversed string (using loop):", reversed_string_loop)