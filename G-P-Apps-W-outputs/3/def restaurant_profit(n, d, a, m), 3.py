
def restaurant_profit(n, d, a, m):
    a.sort()
    profit = 0
    for i in range(m):
        if i < n:
            profit += a[i]
        else:
            profit -= d
    return profit

# Input
n, d = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

# Output
print(restaurant_profit(n, d, a, m))
```
