
def num_button_presses(n, m, a):
    total = 0
    for i in range(n-1):
        if a[i] < a[i+1]:
            total += a[i+1] - a[i]
        else:
            total += m - a[i] + a[i+1]
    return total

def find_min_button_presses(n, m, a):
    min_presses = float('inf')
    for i in range(1, m+1):
        presses = num_button_presses(n, m, [j if j != a[0] else i for j in a])
        min_presses = min(min_presses, presses)
    return min_presses

n, m = map(int, input().split())
a = list(map(int, input().split()))

result = find_min_button_presses(n, m, a)
print(result)
```
