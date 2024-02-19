def print_hourglass(rows):
    # Upper part of the hourglass
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    
    # Lower part of the hourglass
    for i in range(rows - 1, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Example usage with 5 rows
rows = 5
print_hourglass(rows)
