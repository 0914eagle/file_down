
def generate_hard_drive(n, c, b, broken_bits):
    hard_drive = [0] * n
    for i in range(1, n - c + 1):
        if i not in broken_bits:
            hard_drive[i - 1] = 1

    return ''.join(map(str, hard_drive))

# Input parsing
n, c, b = map(int, input().split())
broken_bits = set(map(int, input().split()))

# Generate and print the hard drive pattern
print(generate_hard_drive(n, c, b, broken_bits))
```
