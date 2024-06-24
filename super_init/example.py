# super_init\example.py

# Example to demonstrate how to modify the base class to use super() to call the parent class's __init__ method.


class XDot:
    def __init__(self, x):
        self.x = x
        print(f"XDot __init__: {self.x}")

    def __str__(self):
        return f"XDot: {self.x}"


class Point(XDot):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        print(f"Point __init__: {self.x}, {self.y}")

    def __str__(self):
        return f"Point: {self.x}, {self.y}"


dot = XDot(11)
print("dot: ", dot)

point = Point(22, 33)
print("point: ", point)
