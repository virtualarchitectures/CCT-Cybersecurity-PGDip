# This program counts the number of vowels in a string.

# Prompt the user to enter a string.
input_string = input("Enter a string: ")

# Convert the string to lowercase to handle both uppercase and lowercase vowels.
input_string = input_string.lower()

# Define a string containing all vowels.
vowels = "aeiou"

# Initialize a counter for the number of vowels.
vowel_count = 0

# Iterate through each character in the input string.
for char in input_string:
    # Check if the character is a vowel.
    if char in vowels:
        # If it's a vowel, increment the counter.
        vowel_count += 1

# Print the number of vowels.
print(f"The number of vowels in the string is: {vowel_count}")

#Alternative method using list comprehension.
vowel_count_list = len([char for char in input_string if char in vowels])
print(f"The number of vowels in the string (using list comprehension) is: {vowel_count_list}")