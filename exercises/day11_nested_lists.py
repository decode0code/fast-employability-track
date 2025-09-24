matrix = [[1,2,3], [4,5,6], [7,8,9]]
print("Element at row 2, col 3:", matrix[1][2])


for row in matrix:
    for item in row:
        print(item, end=' ')
    print()

flat = [item for row in matrix for item in row]
print("Flattened list:", flat)

even_numbers = [x for x in flat if x % 2 == 0]
print("Even numbers:", even_numbers)

