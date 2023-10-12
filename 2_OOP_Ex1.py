# Python Object-oriented-programming
# class and object


class Employee:
    def __init__(self, name, age, department, is_manager):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager


E1 = Employee("amine", 23, "informatique", True)
E2 = Employee("ahmed", 25, "physics", False)

print("Employee    Age     department    is_manager")
print(E1.name, "     ", E1.age, "    ", E1.department, "", E1.is_manager)
print(E2.name, "     ", E2.age, "    ", E2.department, "     ", E2.is_manager)


print("______________________________________________________________")
class Student:
    def __init__(self, lastname, firstname, age, CIN, university_name):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.CIN = CIN
        self.university_name = university_name




Stud1 = Student('laakroute', 'amine', 22, 'AAAAA', 'UIT')

print("lastname    firstname    age    CIN    university_name")
print(Stud1.lastname," ", Stud1.firstname,"      ", Stud1.age, "   ", Stud1.CIN,"", Stud1.university_name)



