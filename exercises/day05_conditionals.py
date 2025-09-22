# Day 5 — Conditionals (if / elif / else)
# Run: python exercises/day05_conditionals.py

def basic_checks():
    x = 10
    if x > 0:
        print("x is positive")
    elif x == 0:
        print("x is zero")
    else:
        print("x is negative")

def truthiness_examples():
    items = []
    if items:                      # empty list is Falsey
        print("Has items")
    else:
        print("No items")

def grade_checker():
    # input and validation
    raw = input("Enter marks (0-100): ").strip()
    try:
        marks = float(raw)
    except ValueError:
        print("Invalid input. Please enter a number 0-100.")
        return
    if marks < 0 or marks > 100:
        print("Marks out of range. Enter 0-100.")
        return

    # conditional grading
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Marks: {marks} => Grade: {grade}")
    
    if marks >= 40:
        print("You passed!")
    else:
        print("You failed!")


if __name__ == "__main__":
    print("** Basic checks **")
    basic_checks()
    print("\n** Truthiness examples **")
    truthiness_examples()
    print("\n** Grade checker **")
    grade_checker()
