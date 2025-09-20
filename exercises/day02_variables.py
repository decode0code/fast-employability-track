# exercises/day02_variables.py
"""
Day 2 — Variables, data types, printing, input/output
Run: python exercises/day02_variables.py
"""

def demo_examples():
    # basic variables
    name = "Himanshu"
    age = 25
    height = 5.9
    is_student = True

    # print multiple values
    print(name, age, height, is_student)

    # show types
    print("Types:", type(name), type(age), type(height), type(is_student))

    # formatted printing (f-strings)
    print(f"My name is {name} and I am {age} years old. Height: {height}")

def interactive_part():
    # interactive input (will wait for user)
    user_name = input("Enter your name: ")
    # convert input to float (demonstrates casting)
    marks = float(input("Enter marks (e.g. 85.5): "))
    print(f"{user_name} scored {marks} marks.")

if __name__ == "__main__":
    demo_examples()
    print("\n--- Interactive section below ---")
    interactive_part()


    age = 25
print(f"I am {age} years old.")

