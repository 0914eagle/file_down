
import sys

# s = sys.stdin.readline().strip()
s = input()

if (s[-2] == '3' and (s[-1] == '7' or s[-1] == '9')):
	print('YES')
else:
	print('NO')

