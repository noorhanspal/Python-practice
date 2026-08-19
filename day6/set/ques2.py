# Create a set of numbers and write a program to add, remove, and update elements in the set.
numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)

# Add an element
numbers.add(6)
print("Set after adding 6:", numbers)

# Remove an element
numbers.remove(3)
print("Set after removing 3:", numbers)

# Update an element (remove and add)
numbers.discard(4)
numbers.add(10)
print("Set after updating 4 to 10:", numbers)
