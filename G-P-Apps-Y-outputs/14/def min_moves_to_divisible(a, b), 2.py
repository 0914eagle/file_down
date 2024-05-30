
def min_moves_to_divisible(a, b):
    if a % b == 0:
        return 0
    else:
        return b - a % b

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(min_moves_to_divisible(a, b))
```
