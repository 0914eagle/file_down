
def generate_hard_drive(n, c, b, broken_bits):
    result = [1] * n  # Initialize hard drive with all 1's
    for i in range(b):
        result[broken_bits[i] - 1] = 0  # Set broken bits to 0
    
    current_bit = 0
    for i in range(1, n):
        if result[i-1] != result[i]:
            current_bit += 1  # Count the number of bit changes so far
    
    # Toggle bits to reach c bit changes
    i = n - 2
    while current_bit > c:
        if result[i] != result[i+1]:
            result[i] = 1 - result[i]  # Toggle bit to reduce the number of changes
            current_bit -= 1
        i -= 1
    
    return ''.join(map(str, result))

# Input parsing
inp = input().split()
n, c, b = map(int, inp[:3])
broken_bits = list(map(int, inp[3:]))

print(generate_hard_drive(n, c, b, broken_bits))
```
