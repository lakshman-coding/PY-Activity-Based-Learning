rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
reserved_count = int(input("Enter number of reserved seats: "))
reserved = []

for i in range(reserved_count):
    row_number = int(input("Enter reserved row number: "))
    column_number = int(input("Enter reserved column number: "))
    position = (row_number, column_number)
    reserved.append(position)

print("\nSEATING PLAN")
print("    ", end="")
for column in range(1, columns + 1):
    print("C" + str(column), end=" ")
print()

for row in range(1, rows + 1):
    print("R" + str(row), end="  ")
    for column in range(1, columns + 1):
        position = (row, column)
        if position in reserved:
            symbol = "R"
        elif (row + column) % 2 == 0:
            symbol = "A"
        else:
            symbol = "-"
        print(symbol, end="  ")
    print()
