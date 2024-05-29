
def calculate_entrance(n, a, b):
    return ((a + b - 1) % n) + 1

# Read input
n, a, b = map(int, input().split())

# Calculate the entrance Vasya will end up at
result = calculate_entrance(n, a, b)
print(result)
```
