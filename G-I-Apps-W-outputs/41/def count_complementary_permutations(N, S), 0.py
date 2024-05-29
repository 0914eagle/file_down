
def count_complementary_permutations(N, S):
    def is_complementary(ch1, ch2):
        pair = {"A": "T", "T": "A", "C": "G", "G": "C"}
        return pair[ch1] == ch2

    count = 0
    for start in range(N):
        for end in range(start+1, N+1):
            substring = S[start:end]
            if end - start > 1 and end - start == len(set(substring)):
                complementary_substring = ''.join([{"A": "T", "T": "A", "C": "G", "G": "C"}[ch] for ch in substring])
                if sorted(substring) == sorted(complementary_substring):
                    count += 1
    
    return count

# Read input
N, S = input().split()
N = int(N)
print(count_complementary_permutations(N, S))
```
