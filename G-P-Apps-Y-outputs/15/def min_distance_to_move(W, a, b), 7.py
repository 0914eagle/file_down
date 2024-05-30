
def min_distance_to_move(W, a, b):
    if a <= b <= a + W or a <= b + W <= a + W:
        return 0
    elif b < a:
        return a - (b + W)
    else:
        return b - (a + W)

W, a, b = map(int, input().split())
print(min_distance_to_move(W, a, b))
```
