
def max_chocolates(n, chocolates):
    ans = 0
    for i in range(n):
        ans += min(chocolates[i], sum(chocolates[:i+1]))
    return ans

# Input
n = int(input())
chocolates = list(map(int, input().split()))

# Output
print(max_chocolates(n, chocolates))
```
