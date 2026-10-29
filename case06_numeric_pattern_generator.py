n = int(input("Enter an odd positive dimension: "))

if n <= 0 or n % 2 == 0:
    print("Invalid dimension. Enter a positive odd number.")
else:
    middle = n // 2

    for row in range(middle + 1):
        spaces = middle - row
        width = 2 * row + 1
        print(" " * spaces, end="")
        for column in range(width):
            if column == 0 or column == width - 1 or row == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for row in range(middle - 1, -1, -1):
        spaces = middle - row
        width = 2 * row + 1
        print(" " * spaces, end="")
        for column in range(width):
            if column == 0 or column == width - 1 or row == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
