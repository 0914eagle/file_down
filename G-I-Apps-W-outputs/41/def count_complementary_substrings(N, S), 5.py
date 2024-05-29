
def count_complementary_substrings(N, S):
    count = 0
    for i in range(N):
        freq = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for j in range(i, N):
            freq[S[j]] += 1
            if freq['A'] == freq['T'] and freq['C'] == freq['G']:
                count += 1
    return count

# Input
N, S = input().split()
N = int(N)

# Output
print(count_complementary_substrings(N, S))
```

