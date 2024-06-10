
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def solve(arr, n, m, k):
	counter = [0] * m
	total = 0
	for i in range(n):
		counter[arr[i] - 1] += 1
		total += counter[arr[i] - 1]
	if k >= n:
		return 0
	result = total
	for i in range(n):
		counter[arr[i] - 1] -= 1
		total -= counter[arr[i] - 1]
		if k > 0:
			k -= 1
			total -= 1
		result = min(result, total)
	return result

print(solve(arr, n, m, k))

