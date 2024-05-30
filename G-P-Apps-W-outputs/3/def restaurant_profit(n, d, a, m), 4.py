
def restaurant_profit(n, d, a, m):
    a.sort()
    profit = 0
    for _ in range(m):
        if a[0] < d:
            profit += a[0]
            a[0] = float('inf')
        else:
            profit -= d
        a.sort()
    return profit

# Input
n, d = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

# Output
print(restaurant_profit(n, d, a, m))
```
