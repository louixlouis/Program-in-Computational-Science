# -*- coding: utf-8 -*-
#%%
"""
Problem 1.

The code below uses the bisection search algorithm to find the cube root. However, it works
correctly when 'cube' is a positive number greater than 1. Modify the code so that it also works for
values of 'cube' less than 1.

Hint :
    Exclude the case where 'cube' is negative.
"""

cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
    
#%%
"""
Problem 2.

If you have completed the problem 1, your code works well when 'cube' is positive, cube >= 0.
However, it doesn't function correctly when 'cube' is negative. Based on the code you created for problem 1,
modify it so that it works when 'cube' is negative. 

Hint :
    It should work correctly for the following four cases:
        - cube > 1
        - 0 <= cube <= 1
        - cube < -1
        - -1 <= cube < 0
"""

# TODO
