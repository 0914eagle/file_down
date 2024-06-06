
n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
	a.append(a[i] + a[i + 1])
a = sorted(a)
print(a[-1])
