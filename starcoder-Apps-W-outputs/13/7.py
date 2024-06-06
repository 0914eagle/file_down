
n, x, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        if arr[i] % x == 0 and arr[j] % x == 0 and k >= (arr[j] - arr[i]) // x:
            cnt += 1
print(cnt)
