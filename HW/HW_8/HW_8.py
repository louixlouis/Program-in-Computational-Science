# -*- coding: utf-8 -*-
#%%
"""
Problem 1.

The following function has potential errors. 
Resolve them through exception handling.

If the length of the list parameter is 0, it should return 0. 
If the list parameter is None, it should return the string 'Empty list!'.
"""
def average(numbers):
    result = 0
    for num in numbers:
        result += num
    result /= len(numbers)

    return result

#############################
# Test cases.
# Do not modify below code.
#############################
numbers = [38, 27, 43, 3, 9, 82, 10]
print(average(numbers))
numbers = []
print(average(numbers))
numbers = None
print(average(numbers))

#%%
"""
Problem 2.

While analyzing data, sometimes you may encounter corrupted data. 
In the provided 'student_info' data, 
there are instances where names are missing or scores are entered as negative numbers. 
Implement a function using exception handling to exclude calculations for data with missing names, 
and convert negative scores to positive before calculation.

Given data, this function prints the name and score of the top scorer per grade, 
as well as the average score for each grade.

output example:

Grade 1
Top Scorer: KHQWI, Score: 99
Average Score: 48.75
Grade 2
Top Scorer: DSYBL, Score: 86
Average Score: 40.81
Grade 3
Top Scorer: HDUTZ, Score: 100
Average Score: 45.25

"""

def summarize_student_info(student_info):
    # TODO.
    
#############################
# Test cases.
# Do not modify below code.
#############################
student_info = [{'name': 'PFQYA', 'grade': 3, 'score': 35},
 {'name': 'XBXWN', 'grade': 1, 'score': 32},
 {'name': 'KVDKW', 'grade': 2, 'score': 82},
 {'name': 'CLADT', 'grade': 2, 'score': 12},
 {'name': '', 'grade': 1, 'score': 99},
 {'name': 'GIENO', 'grade': 1, 'score': 52},
 {'name': 'ZWRFR', 'grade': 2, 'score': 2},
 {'name': 'AOJVG', 'grade': 1, 'score': 50},
 {'name': 'TPVOJ', 'grade': 2, 'score': 40},
 {'name': 'DSYBL', 'grade': 2, 'score': 86},
 {'name': '', 'grade': 1, 'score': 37},
 {'name': 'NGTGH', 'grade': 1, 'score': 16},
 {'name': 'HDUTZ', 'grade': 3, 'score': 100},
 {'name': 'CAKSR', 'grade': 1, 'score': 11},
 {'name': 'WIKQY', 'grade': 1, 'score': 92},
 {'name': 'QWABP', 'grade': 3, 'score': 28},
 {'name': 'SWGAP', 'grade': 3, 'score': 80},
 {'name': 'ZZJPU', 'grade': 2, 'score': 11},
 {'name': 'USJEU', 'grade': 1, 'score': 7},
 {'name': 'GHDXV', 'grade': 1, 'score': -43},
 {'name': 'YAYTR', 'grade': 2, 'score': 17},
 {'name': 'VRAEL', 'grade': 1, 'score': 69},
 {'name': 'GZGYS', 'grade': 1, 'score': 95},
 {'name': 'NAQSR', 'grade': 2, 'score': 69},
 {'name': 'VPNMX', 'grade': 2, 'score': 53},
 {'name': 'VTAFF', 'grade': 2, 'score': 26},
 {'name': 'DUSXE', 'grade': 2, 'score': 62},
 {'name': 'WULIZ', 'grade': 3, 'score': -17},
 {'name': 'GHXQA', 'grade': 2, 'score': 76},
 {'name': 'LNYYN', 'grade': 3, 'score': 6},
 {'name': 'LVNGN', 'grade': 1, 'score': 44},
 {'name': 'DQVMB', 'grade': 3, 'score': 30},
 {'name': 'MYQJI', 'grade': 2, 'score': 52},
 {'name': 'ITNJH', 'grade': 2, 'score': -42},
 {'name': 'ASNIV', 'grade': 3, 'score': 66},
 {'name': 'RVNWP', 'grade': 2, 'score': 20},
 {'name': 'KASZV', 'grade': 1, 'score': 26},
 {'name': 'LWUGF', 'grade': 2, 'score': 3},
 {'name': 'WIFGR', 'grade': 1, 'score': 87},
 {'name': 'GPPRF', 'grade': 1, 'score': 20}]

summarize_student_info(student_info)