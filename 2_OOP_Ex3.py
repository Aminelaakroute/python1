# Python Object-oriented-programming
# Class and object and function
# Class Inheritance

class Person:
    def __init__(self, lastname, firstname, age):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
    def display_info(self):
        print(f"Last Name: {self.lastname},  First Name: {self.firstname},  Age: {self.age}")
class Student(Person):
    def __init__(self, lastname, firstname, age, Student_ID):
        # Calling the base class constructor
        super().__init__(lastname, firstname, age)
        self.Student_ID = Student_ID
    def display_info(self):
        # Overriding the display_info method of the base class
        super().display_info()
        print(f"Student Id: {self.Student_ID}")
class Teacher(Person):
    def __init__(self, lastname, firstname, age, Teacher_ID):
        # Calling the base class constructor
        super().__init__(lastname, firstname, age )
        self.Teacher_ID = Teacher_ID
    def display_info(self):
        # Overriding the display_info method of the base class
        super().display_info()
        print(f"Teacher Id: {self.Teacher_ID}")

# Example of use
print("Person")
Person1 = Person('Jones','Charlie',22)
Person1.display_info()
print("_______________________________________________________________________")
print("Student")
Student1 = Student('LAAKR','AMINE',22, 155466)
Student1.display_info()
print("_______________________________________________________________________")
print("Teacher")
Teacher1 = Teacher('Smith','Alice',37, 665849)
Teacher1.display_info()