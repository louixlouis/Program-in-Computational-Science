# -*- coding: utf-8 -*-

#%%
"""
Problem 1.

We're planning to create a university management system. This system will handle student's academic information. 
There are three classes, Student, Class, and School. Implement Class and School classes by utilizing Student class.

Class class has various methods. Leave the __ini__() magic function unmodified and complete the rest of the functions 
to ensure they work properly(Do not modify function parameters).

Complete the whole of School class except __init__(). This class must contain some functions written below.
- get_average() : calculate the school average.
- get_std() : calcaulate the shcool standard deviation
- get_top_student() : find the student with the best score in the school.
- get_bottom_student() : find the student with the worst score in the school.
- add_student() : add student as school member. Place them in the class with the fewest students; if multiple classes have 
the same number of students, add the student to the class with the lowest average. Each class can have up to 5 student, 
and if there are not enough classes, a new class should be added.
- del_student() : delete student from school member.
- __str()__ : When this executed, it print the names and grades of members in each class, along with the class average and standar deviation.
Also, print the total number of members in the school, along with the overall average and standard deviation.
"""
class Student:
    def __init__(self, name, grade, gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa
    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade
    def get_gpa(self):
        return self.gpa
    def set_gpa(self, gpa):
        self.gpa = gpa
    def __str__(self):
        return f'{self.name} / {self.grade}'
    
class Class:
    def __init__(self, name):
        self.name = name
        self.student_list = []
    def get_average(self):
        # Calculate the average of this Class' students gpa
        pass
    def get_std(self):
        # Calculate the standard deviation of this class.
        pass
    def get_top_student(self):
        # find the student with the highest score.
        pass
    def get_bottom_student(self):
        # find the student with the lowest score.
        pass
    def add_student(self, student):
        # Add student as Class member.
        pass
    def del_student(self, name, grade):
        # Delete student from Class member.
        pass
    def __str__(self):
        # When this functions is executed, ensure that it prints the names and grades of the members, 
        # as well as the class average and standard deviation.
        pass

class School:
    def __init__(self, name):
        self.name = name
        self.class_list = []
    # TODO.

#%%
"""
Problem 2.

Implement a banking system using classes. The bank must manage each account with necessary attributes and functions.
Each customer should have a separate account object. Feel free to create the system to satisfy the following conditions:

1. The bank must be able to handle all account information. (creation, deletion, ...)
2. Deposits, withdrawals, and transfers bewteen accounts should be possible.
3. Withdrawals and trasfers should incur a 1% fee.

Think of it as a typical ATM system, which must include balance checking, account management,and password verification processes.
"""

# TODO.
