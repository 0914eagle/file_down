
def kth_character_after_days(S, K):
    days = 5 * 10**15
    for _ in range(days):
        new_S = ''
        for digit in S:
            if digit == '1':
                new_S += '1'
            else:
                new_S += digit * int(digit)
        S = new_S
    return S[K - 1]

# Input
S, K = input().split()
K = int(K)

# Output
print(kth_character_after_days(S, K))
```
