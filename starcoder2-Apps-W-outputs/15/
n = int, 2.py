
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = []
for i in range(n):
    if arr[i] == 0:
        ans.append(arr[i])
for i in range(n):
    if arr[i] != 0:
        if arr[i] % 10 == 0:
            ans.append(arr[i])
print(len(ans))
print(*ans)
