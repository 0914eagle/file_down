
n = int(input())
arr = list(map(int, input().split()))
res = 0
temp = 0
for i in range(len(arr)):
    if i == 0:
        res += 1
        continue
    if arr[i] - arr[i-1] > 0:
        temp = arr[i] - arr[i-1]
    else:
        temp = 1 - (arr[i] - arr[i-1])
    res += abs(temp)
print(res)
