
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prod = 1
for i in range(n):
    for j in range(i+1, n):
        prod *= abs(arr[i] - arr[j])
        prod %= m
print(prod)

