# Inheritance and Polymorphism in Python
import math

# Base class
class Shape:
    def __init__(self, color="white"):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        return (f"{type(self).__name__}: color={self.color}, "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius, color="white"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height, color="white"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side, color="white"):
        super().__init__(side, side, color)


class Triangle(Shape):
    def __init__(self, a, b, c, color="white"):
        super().__init__(color)
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Polymorphism
shapes = [
    Circle(5, "red"),
    Rectangle(4, 6, "blue"),
    Square(3, "green"),
    Triangle(3, 4, 5, "yellow"),
]

for shape in shapes:
    print(shape.describe())

# Multiple inheritance
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
print(f"\nDuck: {duck.fly()}, {duck.swim()}, {duck.quack()}")
print(f"MRO: {[cls.__name__ for cls in Duck.__mro__]}")
