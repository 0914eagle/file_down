
n = int(input())
numbers = list(map(int, input().split()))

def solve(n, numbers):
	sum_values = [0] * n
	prod_values = [1] * n
	for i in range(n):
		sum_values[i] = sum_values[i-1] + numbers[i]
		prod_values[i] = prod_values[i-1] * numbers[i]

	count = 0
	for i in range(n):
		for j in range(i+1, n):
			if sum_values[j] - sum_values[i] == prod_values[j] - prod_values[i]:
				count += 1
	return count

print(solve(n, numbers))

