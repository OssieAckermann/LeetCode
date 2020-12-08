
#Author: Ossie Ackerman
#Created on: 2020/Dec/7

#selection_sort
#Worst-case performance	О(n2) comparisons, О(n) swaps
#Best-case performance	О(n2) comparisons, O(1) swaps
#Average performance	О(n2) comparisons, О(n) swaps


class selection_sort:
    def __init__(self, *array):
        self.array = array

    def sort(self):
        i = 1
        while i < len(self.array):
            j = i
            while j > 0 and self.array[j-1] > self.array[j]:
                self.swap(self.array,j , j-1)
                j -= 1
            i += 1
        print("Array sorted: {}".format(self.array))

    def swap(self, array, a, b):
        pocket = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = pocket

# Demonstration:
import random
array = [random.randint(-100,100) for i in range(10)]
print("Array: {}".format(array))

sorter = insertion_sort()
sorter.array = array
sorter.sort()


