
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = 1
for i in range(n-1):
  for j in range(i+1, n):
    res *= abs(arr[i] - arr[j])
    res %= m
print(res)

