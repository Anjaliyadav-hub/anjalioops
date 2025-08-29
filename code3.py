def print_pyramid(n):
    """Prints a pyramid of * characters."""
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars.strip())


def print_reverse_pyramid(n):
    """Prints a reverse pyramid of * characters."""
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces +  stars.strip())


# --- Main Program ---
rows = int(input("Enter the number of rows: "))

print("\nPyramid:")
print_pyramid(rows)

print("\nReverse Pyramid:")
print_reverse_pyramid(rows)
