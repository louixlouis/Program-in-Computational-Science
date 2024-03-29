# -*- coding: utf-8 -*-
#%%
"""
Problem 1.

Create a function that takes a list of integers as a parameter 
and returns the maximum value.
"""

def find_max(numbers):
    # TODO.


#############################
# Test cases.
# Do not modify below code.
#############################
numbers = [721, 906, 710, 947, 819, 163, 804, 223, 10, 587, 38, 965, 39, 562, 908, 493, 887, 788, 404, 131, 116, 653, 316, 151, 254, 77, 990, 815, 444, 96, 308, 195, 1000, 985, 658, 928, 817, 263, 114, 855, 978, 972, 50, 349, 737, 256, 253, 319, 427, 777, 130, 208, 779, 369, 470, 430, 611, 492, 295, 288, 104, 821, 584, 769, 595, 827, 488, 214, 844, 880, 237, 305, 925, 14, 136, 59, 935, 255, 151, 302, 422, 278, 456, 93, 201, 482, 329, 582, 802, 695, 701, 241, 148, 742, 321, 812, 335, 939, 962, 729, 654, 704, 423, 194, 597, 467, 799, 902, 190, 679, 483, 547, 738, 896, 518, 21, 465, 208, 41, 578, 164, 144, 854, 560, 18, 765, 901, 112, 580, 284, 551, 853, 13, 822, 721, 894, 12, 534, 39, 90, 316, 815, 852, 179, 21, 204, 368, 170, 660, 652, 309, 161, 370, 268, 903, 147, 876, 102, 624, 389, 982, 949, 450, 352, 483, 556, 949, 947, 133, 515, 46, 70, 739, 850, 288, 357, 370, 487, 506, 726, 965, 69, 591, 732, 352, 121, 877, 394, 303, 649, 709, 523, 62, 736, 695, 599, 178, 827, 145, 848, 851, 195, 945, 602, 385, 99, 460, 16, 505, 23, 631, 671, 355, 66, 393, 430, 704, 148, 856, 896, 761, 927, 393, 418, 87, 739, 858, 29, 22, 262, 581, 118, 671, 2, 513, 880, 122, 357, 821, 486, 663, 547, 315, 110, 605, 531, 237, 275, 820, 259, 893, 507, 505, 274, 891, 1000, 697, 680, 966, 861, 905, 684, 38, 107, 40, 991, 554, 690, 371, 91, 988, 731, 114, 682, 445, 849, 795, 531, 538, 932, 376, 828, 171, 499, 391, 298, 501, 915, 37, 188, 125, 737, 628, 755, 726, 47, 790, 428, 710, 261]
print(find_max(numbers))

#%%
"""
Problem 2.

Create a function that takes a list of integers as a parameter 
and returns the list sorted in descending order. 
"""
def descending(numbers):
    # TODO.


#############################
# Test cases.
# Do not modify below code.
#############################
numbers = [721, 906, 710, 947, 819, 163, 804, 223, 10, 587, 38, 965, 39, 562, 908, 493, 887, 788, 404, 131, 116, 653, 316, 151, 254, 77, 990, 815, 444, 96, 308, 195, 1000, 985, 658, 928, 817, 263, 114, 855, 978, 972, 50, 349, 737, 256, 253, 319, 427, 777, 130, 208, 779, 369, 470, 430, 611, 492, 295, 288, 104, 821, 584, 769, 595, 827, 488, 214, 844, 880, 237, 305, 925, 14, 136, 59, 935, 255, 151, 302, 422, 278, 456, 93, 201, 482, 329, 582, 802, 695, 701, 241, 148, 742, 321, 812, 335, 939, 962, 729, 654, 704, 423, 194, 597, 467, 799, 902, 190, 679, 483, 547, 738, 896, 518, 21, 465, 208, 41, 578, 164, 144, 854, 560, 18, 765, 901, 112, 580, 284, 551, 853, 13, 822, 721, 894, 12, 534, 39, 90, 316, 815, 852, 179, 21, 204, 368, 170, 660, 652, 309, 161, 370, 268, 903, 147, 876, 102, 624, 389, 982, 949, 450, 352, 483, 556, 949, 947, 133, 515, 46, 70, 739, 850, 288, 357, 370, 487, 506, 726, 965, 69, 591, 732, 352, 121, 877, 394, 303, 649, 709, 523, 62, 736, 695, 599, 178, 827, 145, 848, 851, 195, 945, 602, 385, 99, 460, 16, 505, 23, 631, 671, 355, 66, 393, 430, 704, 148, 856, 896, 761, 927, 393, 418, 87, 739, 858, 29, 22, 262, 581, 118, 671, 2, 513, 880, 122, 357, 821, 486, 663, 547, 315, 110, 605, 531, 237, 275, 820, 259, 893, 507, 505, 274, 891, 1000, 697, 680, 966, 861, 905, 684, 38, 107, 40, 991, 554, 690, 371, 91, 988, 731, 114, 682, 445, 849, 795, 531, 538, 932, 376, 828, 171, 499, 391, 298, 501, 915, 37, 188, 125, 737, 628, 755, 726, 47, 790, 428, 710, 261]
print(descending(numbers))


#%%
"""
Problem 3.

Create a function that takes two matrices as parameters 
and returns the result of their multiplication. 
If the multiplication of the two matrices is not possible, the function should return -1.
"""

def mat_mul(x, y):
    # x * y
    # TODO.

#############################
# Test cases.
# Do not modify below code.
#############################
x = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
y = [[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]]
print(mat_mul(x, y))
x = [[1, 2],
 [3, 4]]
y = [[5, 6],
 [7, 8],
 [9, 10]]
print(mat_mul(x, y))
x = [[11, 12],
 [13, 14],
 [15, 16],
 [17, 18]]
y = [[19, 20, 21, 22, 23],
 [24, 25, 26, 27, 28]]
print(mat_mul(x, y))

#%%
"""
Problem 4.

Create a function that, given a list of tuples where each tuple contains a name and a score, 
returns a list of the names of the top three scoring individuals, sorted by their scores.
"""

def ranking(data):
    # TODO.

#############################
# Test cases.
# Do not modify below code.
#############################
data = [('Rbegb', 50),
 ('TWeGh', 67),
 ('BVgbx', 24),
 ('vyepQ', 82),
 ('yxvAP', 13),
 ('vsluL', 56),
 ('vPIGl', 57),
 ('LmYYs', 9),
 ('bpQoC', 84),
 ('QyUiM', 70)]

print(ranking(data))
