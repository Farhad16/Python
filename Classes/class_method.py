class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # class method
    @classmethod
    def zero(cls):
        return cls(0, 0, 0)

    @classmethod
    def gives(cls):
        return cls(4, 5, 6)
    # instance method

    def draw(self):
        print(f"{self.x}, {self.y}")

    def sum(self):
        print(self.x+self.y+self.z)


point = Point.gives()
point.sum()
