'''

This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.


'''


def fib(n):
    a, b, c = 0, 1, 0

    for i in range(n-1):
        a, b = b, c
        c = a+b

    return c

if __name__ == "__main__":
    n = int(input())
    print(fib(n))
