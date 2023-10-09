# Python Object-oriented-programming
# class and object and function

class Student:
    def __init__(self, lastname, firstname, age, CIN, note):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.CIN = CIN
        self.note = note

    def Note(self):
        if self.note < 10:
            return "Poor"
        elif (self.note >= 10) and (self.note < 12):
            return "Average"
        elif (self.note >= 12) and (self.note < 14):
            return "Good"
        elif (self.note >= 14) and (self.note <= 16):
            return "Very good"
        else:
            return "Out standing"

# Creation of Student objects
Stud1 = Student('laakr', 'amine', 22, 'AAAAA', 16)
Stud2 = Student('Jones', 'Charlie', 21, 'BBBBB', 18)
Stud3 = Student('Smith', 'Alice', 23, 'CCCCC', 14)
Stud4 = Student('Wilson', 'Henry', 22, 'DDDDD', 12)
Stud5 = Student('Miller', 'Grace', 21, 'EEEEE', 9)
Stud6 = Student('Davis', 'Frank', 20, 'FFFFF', 10)

# Storing Student objects in a list
Student_list = [Stud1, Stud2, Stud3, Stud4, Stud5, Stud6]

# Using the for loop to iterate over the list
for std in Student_list:
    print(f"Last Name: {std.lastname}, First Name: {std.firstname}, Age: {std.age}, CIN: {std.CIN},Note: {std.note},Mention: {std.Note()}")


