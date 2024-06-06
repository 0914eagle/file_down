
'''
Problem : https://www.codechef.com/problems/SAMER08F
Approach : Recursion (Top Down)
'''

import sys

def solve(n, l, r):
	# Base Case
	if n < l:
		return 0

	if n == l:
		return r

	# Solve for [l, r]
	sum = 0
	if l < r:
		sum += 1 + solve(n, l + 1, r)
	else:
		sum += 1 + solve(n - 1, l, r)

	# Solve for [l + 1, r]
	sum += solve(n - 2, l + 1, r)

	return sum

def main():
	n, l, r = map(int, input().split())
	print(solve(n, l, r))

if __name__ == '__main__':
	main()
