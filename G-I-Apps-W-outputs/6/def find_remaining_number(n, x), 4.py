
def find_remaining_number(n, x):
    remaining = x * 2
    return remaining

T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    result = find_remaining_number(n, x)
    print(result)
```
