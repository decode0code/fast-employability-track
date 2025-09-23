# Count down from 5 to 1
num = 5
while num > 0:
    print("Countdown:", num)
    num -= 1


# Count up from 0 to 5
for i in range(0, 6):
    print("Counting up:", i)


for i in range(1, 6):
    if i == 4:
        break  # stop the loop
    if i % 2 == 0:
        continue  # skip even numbers
    print("Loop check:", i)


# ==============================================
# Day 6 – Loops Exercises
# ==============================================

# 1️⃣ While loop: Countdown 5 → 1
print("While loop: Countdown 5 to 1")
num = 5
while num > 0:
    print(num)
    num -= 1

print("\n---------------------\n")

# 2️⃣ For loop: Count up 0 → 5
print("For loop: Count up 0 to 5")
for i in range(0, 6):
    print(i)

print("\n---------------------\n")

# 3️⃣ For loop with step: Even numbers 2 → 10
print("For loop with step: Even numbers 2 to 10")
for i in range(2, 11, 2):
    print(i)

print("\n---------------------\n")

# 4️⃣ For loop counting down: 5 → 1
print("For loop counting down: 5 to 1")
for i in range(5, 0, -1):
    print(i)

print("\n---------------------\n")

# 5️⃣ Loop with break
print("Loop with break at 4")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\n---------------------\n")

# 6️⃣ Loop with continue (skip even numbers)
print("Loop with continue (skip even numbers)")
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

print("\n---------------------\n")

# 7️⃣ Interactive: Count to user-defined number
n = int(input("Enter a number to count up to: "))
for i in range(1, n + 1):
    print(i)

print("\n🎯 Day 6 exercises completed successfully!")

