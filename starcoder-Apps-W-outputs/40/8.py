
from sys import stdin
n = int(input())
s = list(map(str, stdin.readline().strip().split()))

if s.count('?') > 1:
	print("Yes")
elif s.count('?') == 1:
	if s.count('C') and s.count('M'):
		print("Yes")
	elif s.count('C') and s.count('Y'):
		print("Yes")
	elif s.count('Y') and s.count('M'):
		print("Yes")
	else:
		print("No")
else:
	print("No")
