class Point:
    # class label attributes
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)

print(point.color)
Point.color = "Yellow"
point.draw()
print(point.color)
