
def calculate_profit(n, d, a, m):
    sorted_a = sorted(a)
    profit = 0
    for i in range(m):
        if i < n:
            profit += sorted_a[i]
        else:
            profit -= d
    return profit

# Input
n, d = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

# Output
print(calculate_profit(n, d, a, m))
```
