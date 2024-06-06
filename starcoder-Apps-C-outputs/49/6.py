
from sys import stdin

def main():
	X, A, B = map(int, stdin.readline().split())
	digits = stdin.readline().strip()
	ans = 0
	for i in range(A, B + 1):
		i = str(i)
		if all(d in i for d in digits):
			ans += 1
	print(ans)

main()
