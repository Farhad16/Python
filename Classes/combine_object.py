class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(5, 6)
other = Point(10, 20)
farhad = Point("Farhad", 1701)

combined = point + other
print(combined)
print(farhad)
