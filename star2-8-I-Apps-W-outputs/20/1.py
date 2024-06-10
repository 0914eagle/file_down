
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
prod = 1
arr.sort()
for i in range(n-1):
    for j in range(i+1, n):
        prod = (prod * abs(arr[i] - arr[j])) % m
print(prod)

