
def count_sequences(N, K):
    MOD = 10**9 + 7
    
    if N == 1:
        return K
    
    if N == 2:
        return K
    
    if K == 1:
        return 1
    
    if K == 2:
        return 2
    
    result = pow(K, (N + 1) // 2, MOD)
    if N % 2 == 0:
        result += pow(K, N // 2, MOD)
    result %= MOD
    
    return result

# Input parsing
N, K = map(int, input().split())

# Output
print(count_sequences(N, K))
