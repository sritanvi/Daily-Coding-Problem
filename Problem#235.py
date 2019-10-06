'''
This problem was asked by Facebook.

Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.

'''

import sys

def solve(arr):
    min_list = []
    max_list = []
    n = len(arr)
    number_of_comparisons = 0
    for i in range(0, n, 2):
        number_of_comparisons += 1
        temp = max(arr[i], arr[i+1])
        max_list.append(temp)
        min_list.append(arr[i]+arr[i+1]-temp)
        if n % 2 != 0 and i == n-3:
            break
    _min = min_list[0]
    _max = max_list[0]
    for i in range (1, n//2):
        number_of_comparisons += 1
        if max_list[i] > _max:
            _max = max_list[i]

    for i in range(1, n//2):
        number_of_comparisons += 1
        if min_list[i] < _min:
            _min = min_list[i]
    
    if n%2 != 0:
        if _min > arr[-1]:
            _min = arr[-1]
            number_of_comparisons -= 1
        elif _max < arr[-1]:
            _max = arr[-1]

        number_of_comparisons += 2
            
    
    print("minimum element is ",_min, "maximum element is ", _max)
    print("Comprasion number should be less than ", 2 * (n - 2))
    print("Number of comparison are ", number_of_comparisons)

arr = list(map(int, input().split()))
solve(arr)




    
