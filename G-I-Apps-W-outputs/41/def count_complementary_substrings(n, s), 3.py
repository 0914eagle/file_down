
def count_complementary_substrings(n, s):
    def is_complementary(c1, c2):
        return (c1 == 'A' and c2 == 'T') or (c1 == 'T' and c2 == 'A') or (c1 == 'C' and c2 == 'G') or (c1 == 'G' and c2 == 'C')

    def count_permutations(sub_str):
        counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for c in sub_str:
            counts[c] += 1
        
        perm_count = 1
        for key in counts:
            perm_count *= counts[key]
        
        return perm_count
    
    total_count = 0
    for i in range(n):
        for j in range(i, n):
            if j - i + 1 >= 2:
                substr = s[i:j+1]
                complement = ''.join(['T' if ch == 'A' else 'A' if ch == 'T' else 'G' if ch == 'C' else 'C' for ch in substr])
                if substr == complement:
                    total_count += count_permutations(substr)
    
    return total_count

# Input
n, s = input().strip().split()
n = int(n)

# Output
print(count_complementary_substrings(n, s))
```
