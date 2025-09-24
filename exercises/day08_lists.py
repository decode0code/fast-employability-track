# Day 8 — Lists exercises

# Accept numbers either space-separated or comma-separated
user_input = input("Enter numbers separated by space or comma: ")

# Detect separator
if ',' in user_input:
    numbers = [int(num.strip()) for num in user_input.split(',')]
else:
    numbers = [int(num) for num in user_input.split()]

print("Original list:", numbers)
print("Sum:", sum(numbers))
print("Max:", max(numbers), "Min:", min(numbers))

# Squares using list comprehension
squares = [num**2 for num in numbers]
print("Squares:", squares)

# Additional interview-proof methods
numbers.append(100)
print("After append 100:", numbers)

numbers.insert(0, -1)
print("After insert -1 at index 0:", numbers)

if 3 in numbers:
    numbers.remove(3)
    print("After removing 3:", numbers)

popped = numbers.pop()
print("Popped last element:", popped)
print("Final list:", numbers)
