
def count_sequences(N, K):
    if N == 1:
        return K
    if N % 2 == 0:
        return K
    else:
        power = (N + 1) // 2
        return pow(K, power, 10**9 + 7)

N, K = map(int, input().split())
print(count_sequences(N, K))
```
