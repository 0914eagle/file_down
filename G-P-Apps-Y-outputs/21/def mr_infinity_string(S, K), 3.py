
def mr_infinity_string(S, K):
    def transform_string(S):
        new_S = ""
        for char in S:
            if char == '1':
                new_S += '1'
            else:
                count = int(char)
                new_S += count * char
        return new_S

    current_S = S
    for _ in range(5 * 10**15):
        current_S = transform_string(current_S)

    return current_S[K-1]

# Input
S, K = input().split()
K = int(K)

# Output
print(mr_infinity_string(S, K))
```
