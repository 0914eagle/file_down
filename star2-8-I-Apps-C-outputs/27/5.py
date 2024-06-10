
def solve(arr):
	n = len(arr)
	sum_arr = [0] * n
	prod_arr = [0] * n
	for i in range(n):
		if i == 0:
			sum_arr[i] = arr[i]
			prod_arr[i] = arr[i]
		else:
			sum_arr[i] = sum_arr[i - 1] + arr[i]
			prod_arr[i] = prod_arr[i - 1] * arr[i]
	count = 0
	for i in range(n - 1):
		for j in range(i + 1, n):
			if sum_arr[j] - sum_arr[i] == prod_arr[j] - prod_arr[i]:
				count += 1
	return count
n = int(input())
arr = list(map(int, input().split()))
print(solve(arr))

