# Python Object-oriented-programming
# Class and object and function
# Class Inheritance
# Class Abstraction

from abc import abstractmethod, ABC


# Abstract class representing a shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete class representing a circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Concrete class representing a rectangle

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)


# Generic function to display details about a shape
def print_shape_details(shape):
    print(f"Area      : {shape.area()}")
    print(f"Perimeter : {shape.perimeter()}")


# Example of use
circle = Circle(5)
rectangle = Rectangle(4,8)

print("Circle Details :")
print_shape_details(circle)
print("Rectangle Details :")
print_shape_details(rectangle)
