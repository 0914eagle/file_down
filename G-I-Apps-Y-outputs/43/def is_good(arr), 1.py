
def is_good(arr):
    for i, num in enumerate(arr):
        if num == sum(arr) - num:
            return True
    return False

n = int(input())
arr = list(map(int, input().split()))

nice_indices = []
for i in range(n):
    temp = arr[i]
    arr.pop(i)
    if is_good(arr):
        nice_indices.append(i+1)
    arr.insert(i, temp)

if len(nice_indices) == 0:
    print(0)
else:
    print(len(nice_indices))
    print(*nice_indices)
```
