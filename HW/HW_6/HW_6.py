# -*- coding: utf-8 -*-
#%%
"""
Problem 1.

The function implemented below has an aliasing problem.
Solve it by modifying only one line of code.
"""

def sorting(numbers):
    result = numbers
    for pivot_index in range(0, len(result)-1):
        min_val = result[pivot_index]
        min_index = pivot_index
        for cur_index in range(pivot_index, len(result)):
            cur_val = result[cur_index]
            if min_val > cur_val:
                min_val = cur_val
                min_index = cur_index
        result[min_index], result[pivot_index] = result[pivot_index], result[min_index] 
    print(f'Before sorting : {numbers}')
    print(f'After sorting : {result}')

numbers = [721, 906, 710, 947, 819, 163, 804, 223, 10, 587, 38, 965, 39, 562, 908, 493, 887, 788, 404, 131, 116, 653, 316, 151, 254, 77, 990, 815, 444, 96, 308, 195, 1000, 985, 658, 928, 817, 263, 114, 855, 978, 972, 50, 349, 737, 256, 253, 319, 427, 777, 130, 208, 779, 369, 470, 430, 611, 492, 295, 288, 104, 821, 584, 769, 595, 827, 488, 214, 844, 880, 237, 305, 925, 14, 136, 59, 935, 255, 151, 302, 422, 278, 456, 93, 201, 482, 329, 582, 802, 695, 701, 241, 148, 742, 321, 812, 335, 939, 962, 729, 654, 704, 423, 194, 597, 467, 799, 902, 190, 679, 483, 547, 738, 896, 518, 21, 465, 208, 41, 578, 164, 144, 854, 560, 18, 765, 901, 112, 580, 284, 551, 853, 13, 822, 721, 894, 12, 534, 39, 90, 316, 815, 852, 179, 21, 204, 368, 170, 660, 652, 309, 161, 370, 268, 903, 147, 876, 102, 624, 389, 982, 949, 450, 352, 483, 556, 949, 947, 133, 515, 46, 70, 739, 850, 288, 357, 370, 487, 506, 726, 965, 69, 591, 732, 352, 121, 877, 394, 303, 649, 709, 523, 62, 736, 695, 599, 178, 827, 145, 848, 851, 195, 945, 602, 385, 99, 460, 16, 505, 23, 631, 671, 355, 66, 393, 430, 704, 148, 856, 896, 761, 927, 393, 418, 87, 739, 858, 29, 22, 262, 581, 118, 671, 2, 513, 880, 122, 357, 821, 486, 663, 547, 315, 110, 605, 531, 237, 275, 820, 259, 893, 507, 505, 274, 891, 1000, 697, 680, 966, 861, 905, 684, 38, 107, 40, 991, 554, 690, 371, 91, 988, 731, 114, 682, 445, 849, 795, 531, 538, 932, 376, 828, 171, 499, 391, 298, 501, 915, 37, 188, 125, 737, 628, 755, 726, 47, 790, 428, 710, 261]
sorting(numbers)

#%%
"""
Problem 2.

Implement the recurrence relation f(x) = 3f(x-1) + 2f(x-2) using a recursive function.
Note that x is greater than or equals to 2, f(0) = 1, and f(1) = 1.
Do not use any loops.
"""
def recursion(number):
    # TODO.


#############################
# Test cases.
# Do not modify below code.
#############################
print(recursion(5))
print(recursion(10))


#%%
"""
Problem 3.

Convert the recursive function implemented in problem 2 into a version that uses loops
"""

def loop(number):
    # x * y
    # TODO.

#############################
# Test cases.
# Do not modify below code.
#############################
print(loop(5))
print(loop(10))

#%%
"""
Problem 4.

Implement a recursive function to convert a decimal number to binary.
This function's parameter, 'decimal', is integer type, and it should return a string.
Do not use builtin functions, such as bin(), int(), etc.
"""
def dec_to_bin(decimal):
    # TODO.


#############################
# Test cases.
# Do not modify below code.
#############################
if dec_to_bin(1024) == '10000000000':
    print('Correct.')
else:
    print('Wrong.')