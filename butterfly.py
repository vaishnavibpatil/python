def print_butterfly_pattern(size):
    for i in range(size):
        for j in range(i + 1):
            print("*", end=" ")
        spaces = 2 * (size - i - 1)
        for _ in range(spaces):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(size - 1, -1, -1):
        for j in range(i + 1):
            print("*", end=" ")
        spaces = 2 * (size - i - 1)
        for _ in range(spaces):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()

size = int(input("Enter the size of the butterfly pattern: "))
print_butterfly_pattern(size)