
def min_distance(W, a, b):
    if a + W <= b or b + W <= a:
        return max(abs(a + W - b), abs(b + W - a))
    else:
        return 0

# Input
W, a, b = map(int, input().split())

# Output
print(min_distance(W, a, b))
```
