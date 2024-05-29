
def count_possible_sequences(N, K):
    MOD = 10**9 + 7
    if N == 1:
        return K
    if N % 2 == 0:
        return K
    return K**2 % MOD

N, K = map(int, input().split())
print(count_possible_sequences(N, K))
```
