#the property decorator can be used to declare a method as a property object of the class
class Person:
    'Person base class'
    want_to_hack = True
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def print_name(self):
        print('My Name is :{}'.format(self.name))

    def print_age(self):
        print('My Age is:{}'.format(self.__age))



    def birthday(self):
        self.__age =+1

bob = Person ('bob', 25)

print(bob.want_to_hack)
print(bob.getAge)
print(bob.age)