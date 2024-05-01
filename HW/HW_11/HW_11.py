#%%
"""
Problem 1.
Implement a Linear Queue using NumPy's Array that can only store integer data.
'self.size' represents the current number of stored data items,
and 'self.capacity' represents the maximum number of data items that can be stored in the queue.
If the amount of data stored in the queue exceeds 70% of its capacity,
the capacity should be doubled using the 'grow' function.
If the amount of data falls below 30% of its capacity, the capacity should be halved using the 'shrink' function.
However, the capacity should not be decrease below 4.

"""
import numpy as np

class LinearQueue:
    def __init__(self):
        self.array = np.array([None]*4)
        self.front = None
        self.rear = None
        self.size = 0
        self.capacity = 4
    def grow(self):
        # TODO.
    def shrink(self):
        # TODO.
    def enqueue(self, value): 
        # Include code to check the parameters. 
        # For instance, ensure that the parameters are not of 'None' type 
        # and that they are of the correct 'integer' type.
        # TODO.
    def dequeue(self):
        # TODO.
    def __len__(self):
        return self.size

#%%
"""
Problem 2.
Implement the 'get_area' method for a 'Polygon' class.
(reference, https://mathworld.wolfram.com/PolygonArea.html) 

Also, implement the 'get_area' methods for the 'Triangle', 'RightTriangle' and 'Rectangle' classes,
making sure to utilize the method from the superclass in your implementations.
"""
class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # TODO.

class Polygon:
    def __init__(self, *vertices):
        self.vertices = vertices
    def get_vertices(self):
        return self.vertices
    def get_area(self):
        # TODO.

class Triangle(Polygon):
    def __init__(self, *vertices):
        super().__init__(*vertices)
    def get_area(self):
        # TODO.
    
class RightTriangle(Triangle):
    def __init__(self, *vertices):
        super().__init__(*vertices)
    def get_area(self):
        # TODO.
    
class Rectangle(Polygon):
    def __init__(self, *vertices):
        super().__init__(*vertices)
    def get_area(self):
        # TODO.