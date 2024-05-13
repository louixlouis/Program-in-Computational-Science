#%%
"""
Problem 1.
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
    
    def merge_sort(self, reverse=False):
        print('==============MERGE SORT===============')
        result = self.numbers.copy()
        print(f'Original : {result}')
        return result

# Testing code.
numbers = [4, 2, 1, 5, 3, 9, 6, 7]
sorting = Sorting(numbers)
print(f'Test result : {sorted(numbers) == sorting.bubble_sort()}')
print(f'Test result : {sorted(numbers) == sorting.selection_sort()}')
print(f'Test result : {sorted(numbers) == sorting.merge_sort()}')
#%%
"""
Problem 2. Optimization [Greedy Alg]
"""

#%%
"""
Problem 3. Optimization [DP Alg]
"""