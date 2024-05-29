
def count_sequences(N, K):
    MOD = 10**9 + 7
    
    if N == 1:
        return K % MOD
    if N == 2:
        return K % MOD * K % MOD
    
    if N % 2 == 1:
        return pow(K, (N + 1) // 2, MOD)
    else:
        half_seq_count = pow(K, N // 2, MOD)
        return (half_seq_count + K * half_seq_count) % MOD

# Input parsing
N, K = map(int, input().split())

# Output the result
print(count_sequences(N, K))
