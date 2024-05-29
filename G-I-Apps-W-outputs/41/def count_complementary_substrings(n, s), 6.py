
def count_complementary_substrings(n, s):
    complementary_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            if len(set(substr)) == 2 and all(complementary_pairs[substr[k]] == substr[-k-1] for k in range(len(substr)//2)):
                count += 1
                
    return count

# Input
n, s = input().split()
n = int(n)
# Output
print(count_complementary_substrings(n, s))
```
