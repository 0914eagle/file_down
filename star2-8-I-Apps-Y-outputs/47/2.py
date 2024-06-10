
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

def calc(n, p, k, t):
	def calc_factor(n, p, k):
		factor = 1
		for i in range(n):
			factor *= (100 + i * p) / 100
		return factor

	def calc_sum(n, p, k, t):
		sum = 0
		for i in range(n):
			sum += t[i] / (100 + i * p) * 100
		sum += (k - t[n-1]) / 100
		return sum

	factor = calc_factor(n, p, k)
	sum = calc_sum(n, p, k, t)
	return sum / factor

print(calc(n, p, k, t))

