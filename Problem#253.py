"""
This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

"""

def solve(_str, k):

	ra = 0

	_index = 0

	n = len(_str)

	res = [[" " for _ in range(n)] for _ in range(k)]

	_ofset = 0
	
	for s in _str:

		if ra == k:
			_ofset = -1
			ra = k-2
		elif ra == 0:
			_ofset = 1

		res[ra][_index] = s

		_index += 1
		ra += _ofset

	for i in range(k):
		print(*res[i])

if __name__ == "__main__":

	s = input()
	k = int(input())
	solve(s, k)