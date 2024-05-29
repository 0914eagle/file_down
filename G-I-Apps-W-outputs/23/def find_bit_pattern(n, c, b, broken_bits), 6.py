
def find_bit_pattern(n, c, b, broken_bits):
    pattern = [1] * n
    for i in range(0, b):
        pattern[broken_bits[i]-1] = 0

    changes = c
    for i in range(0, n-1):
        if pattern[i] != pattern[i+1]:
            continue
        if changes == 0:
            break
        pattern[i+1] = 1 - pattern[i+1]
        changes -= 1
    
    return ''.join(map(str, pattern))

# Input parsing
n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

# Call the function and output the result
result = find_bit_pattern(n, c, b, broken_bits)
print(result)
```
