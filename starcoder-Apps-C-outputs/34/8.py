
n = int(input())
h, w = [], []
for i in range(n):
	a, b = map(int, input().split())
	h.append(a)
	w.append(b)
h.sort(reverse=True)
w.sort()
print(h[0]*w[0] + h[1]*w[1])
