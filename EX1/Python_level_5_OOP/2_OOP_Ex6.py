# Python Object-oriented-programming
# Class and object and function
# Class Inheritance
# Class Polymorphism

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!!!"


class Cat(Animal):
    def speak(self):
        return "Meow!!!"


class Duck(Animal):
    def speak(self):
        return "Quack!!!"


# Generic function using polymorphism
def animal_sound(animal):
    return animal.speak()


# Example of use
dog = Dog()
cat = Cat()
duck = Duck()
# Polymorphic calls
print("Dog says:", animal_sound(dog))
print("Cat says:", animal_sound(cat))
print("Duck says:", animal_sound(duck))