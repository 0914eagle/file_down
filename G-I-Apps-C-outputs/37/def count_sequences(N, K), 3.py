
def count_sequences(N, K):
    if N == 1:
        return K
    if N % 2 == 0:
        return K
    else:
        return K * K

N, K = map(int, input().split())
result = count_sequences(N, K) % (10**9 + 7)
print(result)
