
def find_entrance(n, a, b):
    return ((a + b - 1) % n) + 1

# Read input values
n, a, b = map(int, input().split())

# Find the entrance number
result = find_entrance(n, a, b)

# Print the result
print(result)
```
