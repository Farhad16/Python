class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"From draw x = {point.x} , y = {point.y}")


point = Point(1, 2)
print(f"x = {point.x} , y = {point.y}")
point.draw()
point.x = 10
point.y = 20

point.draw()
