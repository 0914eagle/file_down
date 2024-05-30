
def min_distance_to_move(W, a, b):
    if a + W <= b or b + W <= a:
        return max(a + W - b, b + W - a)
    else:
        return 0

W, a, b = map(int, input().split())
print(min_distance_to_move(W, a, b))
```
