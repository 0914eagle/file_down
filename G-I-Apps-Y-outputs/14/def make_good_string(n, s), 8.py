
def make_good_string(n, s):
    idx = 1
    result = [s[0]]
    deletions = 0
    
    for i in range(1, len(s)):
        if idx % 2 == 1:
            if s[i] != s[i-1]:
                result.append(s[i])
                idx += 1
            else:
                deletions += 1
        else:
            result.append(s[i])
            idx += 1
    
    return deletions, ''.join(result)

# Read input
n = int(input())
s = input().strip()

# Get the minimum number of deletions and resulting string
deletions, result = make_good_string(n, s)

# Print output
print(deletions)
print(result)
```
