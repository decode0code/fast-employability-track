# Day 4 — Python Operators

# Arithmetic operators
a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)     # float division
print("a // b =", a // b)   # integer division
print("a % b =", a % b)     # modulus
print("a ** b =", a ** b)   # exponent

# Comparison operators
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Assignment operators
c = 5
c += 3  # c = c + 3
print("c after +=3:", c)
c *= 2  # c = c * 2
print("c after *=2:", c)

# Logical operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Bitwise operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 2 =", a << 2) # Left shift
print("a >> 2 =", a >> 2) # Right shift

# Mini calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
