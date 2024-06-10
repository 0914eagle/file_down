
n, k = map(int, input().split())
h = sorted([int(input()) for i in range(n)])
diff = []
for i in range(n - k + 1):
	diff.append(h[i + k - 1] - h[i])

print(min(diff))

