
def solve_hard_drive(n, c, b, broken_bits):
    result = [0] * n
    for i in range(1, n):
        if i not in broken_bits and c > 0:
            result[i] = 1
            c -= 1

    return ''.join(map(str, result))

# Input parsing
n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

# Call the function and print the output
print(solve_hard_drive(n, c, b, broken_bits))
```
