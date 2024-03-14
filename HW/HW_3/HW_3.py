# -*- coding: utf-8 -*-
#%%
"""
Problem 1.

Create a function that takes two parameters: 'option' and 'rows'. 

The 'option' parameter determines the shape of the triangle to be drawn.
If 'option' is 1, the function should draw an upper right triangle; 
if 'option' is 2, it draws a lower right triangle. For any other value, the function prints 'option error.'.

The 'rows' parameter specifies the height of the triangle. If a value less than 2 is entered for 'rows',
the function prints 'rows error'. It is assumed that both 'option' and 'rows' are integers.

For example, if 'draw_triangle(1, 3)' is called, the function should draw an upper right triangle 
with a height of 3 rows as shown below.

***
 **
  *
  
  
if 'draw_triangle(2, 4)' is called, the function should draw an lower right triangle with a height of 4 rows.

   *
  **
 ***
****

"""

def draw_triangle(option, rows):
    # TODO.


#############################
# Test cases.
# Do not modify below code.
#############################
draw_triangle(1, 3)
draw_triangle(2, 4)
draw_triangle(3, 3)
draw_triangle(1, 1)

#%%
"""
Problem 2.

Create a function that draws the same shape of a triangle repeatedly. 

This function must use the triangle drawing function created in the first problem
and takes three parameters: 'option', 'rows', and 'repeat'. 

The roles of 'option' and 'rows' are the same as in the first problem, determining the shape and height of the triangle, respectively.
The 'repeat' parameter specifies how many times the triangle should be drawn repeatedly.
And the 'repeat' parameter must be greater than or equals to 1. If this parameter is less than 1, the function prints 'repeat error'.
It is assumed that all parameters are integer.

For example, if 'repeat_triangle(1, 3, 3)' is called, the function should draw an upper right triangle
with a height of 3 rows, and this triangle should be repeated 3 times as shown below.

***
 **
  *
***
 **
  *
***
 **
  *
  
"""
def repeat_triangle(option, rows, repeat):
    # TODO.


#############################
# Test cases.
# Do not modify below code.
#############################
repeat_triangle(1, 3, 3)
repeat_triangle(2, 4, 5)
repeat_triangle(3, 3, 2)
repeat_triangle(1, 1, 1)
repeat_triangle(1, 4, 0)

#%%
"""
Problem 3.

Create a function converts decimal number to hexadecimal number and return the result.

Hints:
    The 'decimal' parameter is integer type and the result, hexadecimal number, is string type.
    Utilize Python's built-in functions (int(), bin(), oct(), hex())
"""
def dec_to_hex(decimal):
    # TODO.


#############################
# Test cases.
# Do not modify below code.
#############################
if dec_to_hex(100) == '0x64':
    print('Correct')
else:
    print('Wrong')

#%%
"""
Problem 4.

Create a function converts hexadecimal number to decimal number and return the result.

Hints:
    The 'hexadecimal' parameter is string type and the result, decimal number, is integer type.
    Utilize Python's built-in functions (int(), bin(), oct(), hex())
"""

def hex_to_dec(hexadecimal):
    # TODO.

#############################
# Test cases.
# Do not modify below code.
#############################
if hex_to_dec('0xffff') == 65535:
    print('Correct')
else:
    print('Wrong')
