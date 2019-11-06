'''

This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].




'''



def solve(arr):

    n = len(arr)
    res = [0]*n
    if arr[0] > arr[1]:
        res[0] = 2
    else:
        res[0] = 1

    for i in range(1, n-1):
        if arr[i] > arr[i-1]:
            res[i] = res[i-1]+1
        elif arr[i] < arr[i-1]:
            if arr[i] < arr[i+1]:
                res[i] = 1
            elif arr[i] > arr[i+1]:
                j = i
                count = 2
                while j != n-1 and arr[j+1] > arr[j]:
                    count+=1
                    j+=1
                res[i] = count
            else:
                res[i] = res[i-1]
    if arr[n-1] > arr[n-2]:
        res[n-1] = res [n-2] + 1
    elif arr[n-1] < arr[n-2]:
        res[n-1] = 1
    else:
        res[n-1] = res[n-1]
    return res


if __name__ == "__main__":

    arr = list(map(int, input().split()))
    res = solve(arr)
    print(res)

