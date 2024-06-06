


for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	a = a + [0] + a[::-1]
	c = 0
	for i in range(1, len(a) - 1):
		if a[i - 1] < a[i] > a[i + 1] or a[i - 1] > a[i] < a[i + 1]:
			c += 1
	print("YES" if c % 2 == 0 else "NO")

