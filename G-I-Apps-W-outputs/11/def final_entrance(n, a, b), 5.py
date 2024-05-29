
def final_entrance(n, a, b):
    return (a + b - 1) % n + 1

# Input
n, a, b = map(int, input().split())

# Output
print(final_entrance(n, a, b))
```
