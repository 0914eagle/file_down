
def calculate_profit(n, d, a, m):
    a.sort()
    profit = 0
    for i in range(m):
        if i < n:
            profit += a[i]
        else:
            profit -= d
    return profit

n, d = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

result = calculate_profit(n, d, a, m)
print(result)
```
