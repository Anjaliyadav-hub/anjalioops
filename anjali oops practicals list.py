import cmath  # To handle complex numbers

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = (b**2) - (4*a*c)

# Calculate roots
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

# Display results
print(f"\nThe roots of the equation {a}x² + {b}x + {c} = 0 are:")
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
