
def minimum_steps(n, arr):
    steps = 0
    prev = 0
    for i in range(n):
        steps += abs(arr[i] - prev)
        prev = arr[i]
    return steps

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(minimum_steps(n, arr))
```
