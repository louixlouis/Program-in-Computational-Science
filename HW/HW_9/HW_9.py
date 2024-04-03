# -*- coding: utf-8 -*-
#%%
"""
Problem 1.

Complete the __init__() method of a class that has name, grade, gpa and gender as attributes. 
You need to modify both the parameters and the function statement.
"""
class Student:
    def __init__(///////):
        ///////

#%%
"""
Problem 2.

"info_list" contains tuples of (name, grade, gpa, gender). 
Using each element of this list, you aim to create objects of the Student class made in problem 1. 
Complete the creation of "student_object_list", which contains objects of the Student class, 
using list comprehension.

Write your code for list comprehension in a single line.
"""


info_list = [
    ('azfDVaR', 2, 4.26, 'woman'),
    ('bwetEU', 1, 3.13, 'woman'),
    ('ggKuaO', 1, 3.6, 'woman'),
    ('OqenbOb', 3, 3.13, 'man'),
    ('lLPDBzbmW', 4, 3.83, 'man'),
    ('FoUNJaeFVu', 4, 3.14, 'man'),
    ('geKSF', 4, 3.56, 'man'),
    ('MMaOEPTd', 4, 3.73, 'man'),
    ('oRvYhDy', 1, 4.02, 'woman'),
    ('CKlLxMB', 2, 3.66, 'woman'),
    ('AKRmwcb', 3, 3.93, 'man'),
    ('qcAxzVLHCa', 1, 3.94, 'woman'),
    ('gnVyaPa', 4, 3.64, 'woman'),
    ('qpPOKxfN', 4, 3.89, 'man'),
    ('gZtKF', 3, 3.25, 'man'),
    ('lQdDhcP', 3, 3.73, 'man'),
    ('dlaBjICPSH', 2, 3.05, 'man'),
    ('pszOihSMo', 4, 4.21, 'man'),
    ('RUrpHhvB', 2, 3.22, 'man'),
    ('XFNSvEyA', 4, 3.81, 'woman')]

student_object_list = # Fill this line.
    
#%%
"""
Problem 3.

Create a function that analyzes grades given a student_object_list as an argument, 
which was created in problem 2. This function needs to calculate the following:

    Average grade for female students.
    Average grade for male students.
    Average grade by grade level.
    Name of the top-performing female student.
    Name of the top-performing male student.
    Name of the top-performing student by grade level.

You must not use if statements but must utilize match statements instead.
You can implement several functions if you need.

Output foramt:
    Average grade for female students : 4.3
    Average grade for male students : 4.3
    Average grade by grade level : grade 1(4.3) grade 2(4.3) grade 3(4.3) grade 4(4.3)
    Name of the top-performing female student is "her name" (Do not contain quotation marks)
    Name of the top-performing male student is "his name"
    Name of the top-performing student by grade level : grade 1(name) grade 2(name) grade 3(name) grade 4(name)
"""
def analysis(student_object_list):
    # TODO.

analysis(student_object_list)