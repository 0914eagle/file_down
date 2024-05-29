
def remaining_number(n, x):
    ans = 2 * x
    return ans

T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    result = remaining_number(n, x)
    print(result)
```
