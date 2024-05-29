
def count_same_content_subsequences(N, M, S, T):
    MOD = 10**9 + 7

    # Construct a dictionary to store the frequency of each subsequence in S
    freq_s = {}
    for i in range(1, 1 << N):
        subseq = []
        for j in range(N):
            if i & (1 << j):
                subseq.append(S[j])
        freq_s[tuple(subseq)] = freq_s.get(tuple(subseq), 0) + 1

    # Calculate the number of pairs of same content subsequences in S and T
    res = 0
    for i in range(1, 1 << M):
        subseq = []
        for j in range(M):
            if i & (1 << j):
                subseq.append(T[j])
        res += freq_s.get(tuple(subseq), 0)

    return res % MOD

# Read input N, M, S, T
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# Call the function and print the result
print(count_same_content_subsequences(N, M, S, T))
```
