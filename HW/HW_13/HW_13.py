#%%
"""
Problem 1.
Write a python class Item with attributes like name, price, stock, and methods like get/set and some useful methods.
"""

class Item:
    # TODO
    pass

#%%
"""
Problem 2.
Write python classes Table, TwoTable, and FourTable with attributes like capacity(the number of seats), 
book(boolean type, reservation status), empty(boolean type, whether this table is empty), 
and methods like get/set and some useful methods.

The Table class is the superclass of TwoTable and FourTable. TwoTable represents a table for two people, 
and FourTable represents a table for four people.

Considering their relationshipm, write code freely.
"""

class Table:
    # TODO
    pass

class TwoTable(Table):
    # TODO
    pass

class FourTable(Table):
    # TODO
    pass

#%%
"""
Problem 3.
Create a Restaurant class using the classes from problems 1 and 2. 
The Restaurant should have ten 2-person tables and ten 4-person tables. The menu should have five items, which tou can specify freely.

Implement the functions necessary for restaurant operations:

1. Table reservation : Groups of 1-2 people should use 2-person tables, and groups of 3-4 people should use 4-person tables. 
For groups of 5 or more, a combination of 4-person and 2-person tables should be used. 
Implement a function using reservation numbers to handle this.

2. Ordering : Orders should be taken per table, and payment information should be saved. 
When ordering food, the stock status of the food must be checked.

3. Payment : Payments should be processed per table. Once payment is completed, the table should be marked as empty.
"""

class Restaurant:
    #TODO
    pass