'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

def solution(arr, k):

    count_dict = {}

    for i in arr:
        if k-i in count_dict:
            return True
        else:
            count_dict[i] = True

    return False



print(solution(list(map(int, input().split())), int(input())))




