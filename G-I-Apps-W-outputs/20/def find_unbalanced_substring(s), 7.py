
def find_unbalanced_substring(s):
    n = len(s)
    
    for i in range(n-1):
        for j in range(i+1, n):
            substring = s[i:j+1]
            count = {}
            for char in substring:
                count[char] = count.get(char, 0) + 1
            max_freq = max(count.values())
            if max_freq > len(substring) // 2:
                return i+1, j+1
    
    return -1, -1

# Input
s = input().strip()

# Find unbalanced substring
a, b = find_unbalanced_substring(s)

# Output
print(a, b)
```
