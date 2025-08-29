import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other):
        if not isinstance(other, Point):
            raise ValueError("The argument must be a Point object")
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)


# Example usage
p1 = Point(3, 4)
p2 = Point(7, 1)

print(p1)  # Output: Point(3, 4)
print(p2)  # Output: Point(7, 1)

dist = p1.distance(p2)
print(f"Distance between {p1} and {p2} is {dist:.2f}")

