
def CRT(m, a):
	M = 1
	for i in m:
		M *= i
	ans = 0
	for i in range(len(m)):
		ans += a[i] * M // m[i] * pow(M // m[i], m[i] - 2, m[i])
	return ans % M


def solve(m, x, y):
	lo = 0
	hi = 2 ** 60
	while lo < hi:
		mid = (lo + hi) // 2
		if all([abs((mid - x[i]) % m[i]) <= y[i] for i in range(len(m))]):
			hi = mid
		else:
			lo = mid + 1
	return lo


m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(solve(m, x, y))

