
def count_sequences(N, K):
    if N == 1:  # If there is only one element in the sequence
        return K
    if N == 2:  # If there are two elements in the sequence
        return K * K % (10**9 + 7)
    
    return pow(K, (N + 1) // 2, 10**9 + 7)

# Read input
N, K = map(int, input().split())

# Calculate and print the number of sequences
result = count_sequences(N, K)
print(result)
