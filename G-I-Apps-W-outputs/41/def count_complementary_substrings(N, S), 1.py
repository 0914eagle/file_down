
def count_complementary_substrings(N, S):
    def is_complementary(a, b):
        return (a == 'A' and b == 'T') or (a == 'T' and b == 'A') or \
               (a == 'C' and b == 'G') or (a == 'G' and b == 'C')

    def count_permutations(c):
        return (c * (c - 1)) // 2
    
    count = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            substring = S[i:j]
            substr_count = dict()
            complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            for char in substring:
                if char not in substr_count:
                    substr_count[char] = 0
                substr_count[char] += 1
        
            is_valid = True
            for key in substr_count:
                if substr_count[key] != substr_count.get(complement[key], 0):
                    is_valid = False
                    break
            
            if is_valid:
                c = sum(v for v in substr_count.values())
                count += count_permutations(c)
    
    return count

# Input reading
N, S = input().split()
N = int(N)
print(count_complementary_substrings(N, S))
```
