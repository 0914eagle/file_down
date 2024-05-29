
def count_complementary_substrings(N, S):
    count = 0
    for i in range(N):
        for j in range(i+1, N+1):
            substr = S[i:j]
            len_substr = len(substr)
            if len_substr % 2 != 0:
                continue
            half_len = len_substr // 2
            complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
            permuted_substr = ''.join(complement[c] for c in substr[::-1])
            if substr.count('A') == substr.count('T') and substr.count('C') == substr.count('G'):
                if substr[:half_len] == permuted_substr[:half_len]:
                    count += 1
    return count

# Read input
N, S = input().split()
N = int(N)
result = count_complementary_substrings(N, S)
print(result)
```
