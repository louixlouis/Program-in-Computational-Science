#%%
"""
Problem 1.
In the Sorting class, there are three types of sorting algorithms (ascending order) implemented. 
Modify the code so that when the reverse parameter is set to true, the sorting is done in descending order. 
Note that you cannot use the reverse() function.
"""

class Sorting:
    def __init__(self, numbers):
        self.numbers = numbers.copy()
    
    def bubble_sort(self, reverse=False):
        print('==============BUBBLE SORT==============')
        result = self.numbers.copy()
        print(f'Original : {result}')
        swap = False
        while not swap:
            swap = True
            for i in range(len(result)-1):
                if result[i] > result[i+1]:
                    swap = False
                    result[i], result[i+1] = result[i+1], result[i]
                    print(f'Swap {result[i+1]} <----> {result[i]}', end=' ')
                    print(result)
        return result
    
    def selection_sort(self, reverse=False):
        print('============SELECTION SORT=============')
        result = self.numbers.copy()
        print(f'Original : {result}')
        for i in range(len(result)-1):
            for j in range(i, len(result)):
                if result[j] < result[i]:
                    result[j], result[i] = result[i], result[j]
                    print(f'Swap {result[i]} <----> {result[j]}', end=' ')
                    print(result)
        return result
    
    def merge(self, left, right):
        print(f'Left : {left}')
        print(f'Right : {right}')
        print('---------------------------------------')
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    def merge_sort(self, numbers, reverse=False, is_first=False):
        if is_first:
            print('==============MERGE SORT===============')
            print(f'Original : {numbers}')
        
        if len(numbers) < 2:
            return numbers[:]
        else:
            middle = len(numbers) // 2
            left = self.merge_sort(numbers[:middle])
            # print(f'Left : {left}')
            right = self.merge_sort(numbers[middle:])
            # print(f'Right : {right}')
            return self.merge(left, right)

# Testing code.
numbers = [4, 2, 1, 5, 3, 9, 6, 7]
sorting = Sorting(numbers)
print(f'Test result : {sorted(numbers) == sorting.bubble_sort()}')
print(f'Test result : {sorted(numbers) == sorting.selection_sort()}')
print(f'Test result : {sorted(numbers) == sorting.merge_sort(numbers, is_first=True)}')
#%%
"""
Problem 2.
Refer to Lecture 1 to implement the greedy algorithm and the test function. 
Note that you cannot modify any parts other than the # TODO sections.
"""
class Food:
    def __init__(self, name, value, calories):
        self.name, self.value, self.calories = name, value, calories
    def get_value(self):
        return self.value
    def get_cost(self):
        return self.calories
    def get_density(self):
        return self.get_value() / self.get_cost()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def greedy(items, max_cost, key_func):
    # TODO
    pass

def test_greedy(items, constraint, key_func):
    # TODO
    pass

def test_greedys(items, constraint, key_func):
    # TODO
    pass

menu = (('wine', 89, 123), ('beer', 90, 154), ('pizza', 30, 258), ('burger', 50, 354), ('fries', 90, 365), ('coke', 79, 150), ('apple', 90, 95), ('donut', 10, 195))
items = []
for item in menu:
    items.append(Food(*item))
test_greedys(800)