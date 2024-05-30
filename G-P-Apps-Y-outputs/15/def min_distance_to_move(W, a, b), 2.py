
def min_distance_to_move(W, a, b):
    if a <= b <= a + W or b <= a <= b + W:
        return 0
    return min(abs(b - (a + W)), abs(a - (b + W))

W, a, b = map(int, input().split())
print(min_distance_to_move(W, a, b))
```
