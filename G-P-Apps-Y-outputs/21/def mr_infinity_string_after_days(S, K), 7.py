
def mr_infinity_string_after_days(S, K):
    n = len(S)
    count = [0] * n

    current_sum = 0
    for i in range(n):
        current_sum += int(S[i])
        count[i] = current_sum

    day = 0
    while day < 5 * 10**15:
        new_S = ''
        for i, char in enumerate(S):
            new_S += char * count[i]
        S = new_S
        day += 1

    return S[K-1]

# Input processing
S, K = input().split()
K = int(K)

print(mr_infinity_string_after_days(S, K))
```
