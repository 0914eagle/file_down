
def find_bit_pattern(n, c, b, broken_bits):
    bit_pattern = ['0'] * n
    bit_changes = c

    for i in range(1, n - 1):
        if i not in broken_bits and bit_changes > 0:
            bit_pattern[i] = '1'
            bit_changes -= 1

    return ''.join(bit_pattern)

n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

print(find_bit_pattern(n, c, b, broken_bits))
```
