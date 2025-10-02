# Function to calculate the area of a rectangle.
def calculate_area(length, width):
    """
    This function calculates the area of a rectangle.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    area = length * width
    return area

# Call the calculate_area function with different dimensions and print the returned area.
area1 = calculate_area(5, 10)
print(f"Area 1: {area1}")

area2 = calculate_area(8, 8)
print(f"Area 2: {area2}")

area3 = calculate_area(3, 12)
print(f"Area 3: {area3}")

#Example with negative numbers, which is technically incorrect for real-world areas, but still works mathematically.
area4 = calculate_area(-4, 6)
print(f"Area 4: {area4}")