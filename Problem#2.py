'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

'''

import math

def solve(arr):
    new_arr = []
    res = 0

    for i in arr:
        res += math.log(i, 10)
    
    for i in arr:
        new_arr.append(res-math.log(i, 10))



    for i in range(len(arr)):
        new_arr[i] = round(10**(new_arr[i]))

    return new_arr


print(*solve(list(map(int, input().split()))))


