#%%
"""
Problem 1.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_next(self):
        return self.next
    def set_next(self, node):
        self.next = node

class LinearQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self, value):   # None이 들어오는 경우 처리하기.
        new_node = Node(value)
        if self.size == 0:
            self.front = new_node
            self.rear = self.front
        else:
            new_node.set_next(self.front)
            self.front = new_node
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.front = self.front.get_next()
        self.size -= 1
    def __len__(self):
        return self.size
    