'''

This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be 5.


'''



def solve(n, k):
    if n == 1:
        return k
    elif k <= 1:
        return k

    _min = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    
    for i in range(1, k+1):

        temp = max(solve(n-1, i-1), solve(n, k-i))

        if temp < _min:
            _min = temp

    return _min + 1


if __name__ == "__main__":

    n = int(input())
    k = int(input())
    print(solve(n, k))
