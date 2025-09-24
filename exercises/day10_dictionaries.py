# Day 10: Dictionaries in Python

# 1. Create dictionary
student = {
    "name": "Himanshu",
    "age": 33,
    "marks": 95
}

# 2. Print keys and values
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 3. Add a new key
student["city"] = "Delhi"
print("After adding city:", student)

# 4. Update marks
student["marks"] = 98
print("After updating marks:", student)

# 5. Remove age
student.pop("age")
print("After removing age:", student)

# 6. Iterate over dictionary
for key, value in student.items():
    print(f"{key} => {value}")
