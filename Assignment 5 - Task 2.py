# Assignment 5: Task 2 - List Slicing
# Module 6: Data Structures and Strings in Python

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original list (1 to 10):")
print(numbers)

# Extract the first five elements from the list
first_five = numbers[:5]
print("\nFirst five elements (using slicing [0:5]):")
print(first_five)

# Reverse the extracted elements
reversed_list = first_five[::-1]
print("\nReversed first five elements:")
print(reversed_list)

# Display summary
print("\n" + "=" * 50)
print("Summary:")
print(f"Original list:          {numbers}")
print(f"First five elements:    {first_five}")
print(f"Reversed list:          {reversed_list}")
print("=" * 50)
