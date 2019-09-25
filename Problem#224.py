'''
This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

'''

def solve(arr):

    n = len(arr)
    res = 1

    for i in range(n):

        if arr[i] <= res:
            res += arr[i]
        else:
            break
    return res


arr = list(map(int, input().split()))
print(solve(arr))
