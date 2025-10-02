# This program checks if a string is a palindrome.

# Prompt the user to enter a string.
input_string = input("Enter a string: ")

# Remove spaces and convert the string to lowercase for case-insensitive comparison.
cleaned_string = "".join(input_string.split()).lower()

# Reverse the cleaned string using string slicing.
reversed_string = cleaned_string[::-1]

# Check if the cleaned string is equal to its reversed version.
if cleaned_string == reversed_string:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

# Alternative method using a loop and comparing characters.
# Initialize two pointers, one at the beginning and one at the end.
left = 0
right = len(cleaned_string) - 1
is_palindrome_loop = True  # Assume it's a palindrome initially

# Loop until the pointers meet or cross each other.
while left < right:
    # If the characters at the pointers are different, it's not a palindrome.
    if cleaned_string[left] != cleaned_string[right]:
        is_palindrome_loop = False
        break  # Exit the loop early
    # Move the pointers towards the center.
    left += 1
    right -= 1

# Print the result based on the loop.
if is_palindrome_loop:
    print(f"'{input_string}' (checked by loop) is a palindrome.")
else:
    print(f"'{input_string}' (checked by loop) is not a palindrome.")