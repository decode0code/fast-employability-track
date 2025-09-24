# Tuple creation
fruits = ("apple", "banana", "cherry")
print(f"Tuple: {fruits}")

# Access elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Length
print("Number of fruits:", len(fruits))

# Tuples are immutable
# fruits[0] = "orange"  # This will raise an error

# Set creation
numbers = {1, 2, 3, 2, 1}
print(f"Set (duplicates removed): {numbers}")

# Add elements
numbers.add(4)
print("After adding 4:", numbers)

# Remove elements
numbers.remove(3)
print("After removing 3:", numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)

