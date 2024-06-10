
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(n - 2):
    a = arr[i]
    for j in range(i + 1, n - 1):
        b = arr[j]
        c = a + b
        if c in arr[j + 1:]:
            ans += 1
print(ans)

