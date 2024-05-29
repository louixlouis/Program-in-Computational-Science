#%%
"""
Problem 1.
"""

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = x
        self.z = z

class RightTriangle:
    def __init__(self, pt1, pt2, pt3):
        self.points = [pt1, pt2, pt3]

    def get_area(self):
        return None
    
class rectangle(RightTriangle):
    def __init__(self, pt1, pt2, pt3):
        super().__init__(pt1, pt2, pt3)

    def get_area(self):
        super().get_area()

class Cube(rectangle):
    def __init__(self, pt1, pt2, pt3, pt4, pt5, pt6):
        self.faces = []
    
    def get_area(self):
        super().get_area()

    def get_volume(self):
        # TODO.
        pass

#%%
"""
Problem 2.
"""
class Animal:
    pass

class Mammal(Animal):
    pass

class Primate(Mammal):
    pass

class Human(Primate):
    pass

