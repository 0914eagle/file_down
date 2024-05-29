
def generate_bit_pattern(n, c, b, broken_bits):
    result = ['1'] * n
    count = 0
    for i in range(1, n):
        if i not in broken_bits and count < c:
            result[i] = '0' if result[i-1] == '1' else '1'
            count += 1
    return ''.join(result)

n, c, b = map(int, input().split())
broken_bits = set(map(int, input().split()))
print(generate_bit_pattern(n, c, b, broken_bits))
```
