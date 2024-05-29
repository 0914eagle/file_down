
def num_presses(n, m, a):
    total_presses = abs(a[0] - a[1])
    for i in range(1, n - 1):
        diff = abs(a[i] - a[i + 1])
        total_presses += min(diff, m - diff)
    
    return total_presses

n, m = map(int, input().split())
a = list(map(int, input().split()))

min_presses = float('inf')
for x in range(1, m + 1):
    presses = num_presses(n, m, [x] + a)
    if presses < min_presses:
        min_presses = presses

print(min_presses)
```
