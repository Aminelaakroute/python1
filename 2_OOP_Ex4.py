# Python Object-oriented-programming
# Class and object and function
# Class Encapsulation

class Person:
    def __init__(self, lastname, firstname, age):
        self._lastname = lastname    # Protected attribute
        self._firstname = firstname  # Protected attribute
        self._age = age              # Protected attribute

    # Read access methods (getter)
    def get_last_name(self):
        return self._lastname

    def get_first_name(self):
        return self._firstname

    def get_age(self):
        return self._age

    # Write access methods (setter)
    def set_last_name(self, Lastname):
        self._lastname = Lastname

    def set_first_name(self, Firstname):
        self._firstname = Firstname

    def set_age(self, Age):
        if Age > 0:
            self._age = Age
        else:
            print("Age cannot be negative.")


person1 = Person('Laakroute', 'Amine', 22)


# Access to attributes via getter methods

print(f"Last  Name : {person1.get_last_name()}")
print(f"First Name : {person1.get_first_name()}")
print(f"Age        : {person1.get_age()}")
print("____________________________________________________")
# Modifying attributes via setter methods
person1.set_last_name('Jones')
person1.set_first_name('Charlie')
person1.set_age(21)
print(f"Last  Name : {person1.get_last_name()}")
print(f"First Name : {person1.get_first_name()}")
print(f"Age        : {person1.get_age()}")





