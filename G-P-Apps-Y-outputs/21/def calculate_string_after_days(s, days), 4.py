
def calculate_string_after_days(s, days):
    for _ in range(days):
        new_s = ''
        for digit in s:
            if digit == '1':
                new_s += '1'
            else:
                new_s += digit * int(digit)
        s = new_s
    return s

# Input
S, K = input().split()
K = int(K)
result = calculate_string_after_days(S, 5 * 10**15)

# Output
print(result[K-1])
```
