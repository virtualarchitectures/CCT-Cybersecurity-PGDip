def min_max(numbers):
    """
    Finds the minimum and maximum values in a list of numbers.

    Args:
        numbers: A list of numbers (can be integers or floating-point numbers).

    Returns:
        A tuple containing the minimum and maximum values, in that order (min, max).
        Returns (None, None) if the input list is empty, indicating that there's no min or max.

    Example:
        min_max([1, 5, 2, 8, -3])  # Returns (-3, 8)
        min_max([])  # Returns (None, None)
    """

    # Check if the list is empty.  If it is, we can't find a min or max,
    # so we return (None, None). This prevents errors later on.
    if not numbers:
        return (None, None)

    # Initialize both the minimum (min_val) and maximum (max_val) values
    # to the FIRST element of the list.  This is important because:
    #   - It works correctly even if the list contains negative numbers.
    #   - It handles the case where the list has only one element correctly.
    min_val = numbers[0]
    max_val = numbers[0]

    # Now, we iterate (loop) through the rest of the numbers in the list.
    # The 'for' loop goes through each number, one at a time.
    for number in numbers:
        # Check if the current 'number' is smaller than the current 'min_val'.
        # If it is, we've found a new minimum, so we update 'min_val'.
        if number < min_val:
            min_val = number

        # Check if the current 'number' is larger than the current 'max_val'.
        # If it is, we've found a new maximum, so we update 'max_val'.
        if number > max_val:
            max_val = number

    # After the loop has finished, 'min_val' will hold the smallest number
    # in the list, and 'max_val' will hold the largest number.
    # We return them as a tuple: (min_val, max_val).
    return (min_val, max_val)


# --- Example Usage and Test Cases ---

# Here are some examples to show how the function works and to test it
# with different kinds of input.  Good tests are essential for making sure
# your code works correctly!

test_cases = [
    ([1, 2, 3, 4, 5], (1, 5)),  # List in ascending order
    ([5, 4, 3, 2, 1], (1, 5)),  # List in descending order
    ([-1, 0, 1, 2, 3], (-1, 3)),  # List with negative numbers
    ([10, 10, 10, 10], (10, 10)),  # List with all the same numbers
    ([-5, -2, -8, -1], (-8, -1)),  # List with only negative numbers
    ([42], (42, 42)),  # List with a single element
    ([], (None, None)),  # Empty list - special case!
    ([1.5, 2.7, 0.3, 5.1], (0.3, 5.1)),  # List with floating-point numbers
]

# This loop goes through each test case.
for numbers, expected in test_cases:
    # Call the 'min_max' function with the input list.
    result = min_max(numbers)

    # Print the results in a clear way, showing:
    #   - The input list
    #   - The result returned by the function
    #   - The expected (correct) result
    #   - Whether the test passed (result == expected)
    print(f"Input: {numbers}, Output: {result}, Expected: {expected}, Pass: {result == expected}")

#  Key Concepts Explained:
#
#  * List:  An ordered collection of items (in this case, numbers).  You can access items by their index (position).
#  * Tuple:  Similar to a list, but it's *immutable* (you can't change it after it's created).  Used here to return multiple values.
#  * `for` loop:  A way to repeat a block of code for each item in a sequence (like a list).
#  * `if` statement:  A way to execute a block of code only if a certain condition is true.
#  * Function:  A reusable block of code that performs a specific task.  It takes input (arguments) and can return output.
#  * Docstring: The text inside the triple quotes (""") at the beginning of the function.  It explains what the function does.
#  * Variable:  A name that refers to a value (like 'min_val', 'max_val', 'number').
#  * Initialization: Setting the initial value of a variable (like setting 'min_val' and 'max_val' to the first element).
#  * Edge Case:  A specific input or situation that might cause problems if not handled carefully (like an empty list).
#  * Test Cases:  Examples used to verify that a function works correctly for different inputs.
#  * Time Complexity: How the runtime of the function scales with the input size (O(n) means it's proportional to the number of elements).