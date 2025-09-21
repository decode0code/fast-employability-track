# Day 3 — Input and Data Types

# Taking input as a string
name = input("Enter name: ")
print(f"Hello, {name}!")

# Taking numeric input (but input() always returns a string!)
age = input("Enter age: ")
print(f"Type of age before conversion: {type(age)}")

# Convert string to integer
age = int(age)
print(f"I am {age} years old.")
print(f"Type of age after conversion: {type(age)}")
# Example calculation with numeric input
birth_year = 2025 - age
print(f"You were born in {birth_year}.")
