
def make_good_string(n, s):
    result = []
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            result.append(i)
    
    deleted = 0
    new_s = ""
    for i in range(len(s)):
        if i in result:
            deleted += 1
        else:
            new_s += s[i]
    
    return deleted, new_s

# Input parsing
n = int(input())
s = input().strip()

# Solve the problem
deleted, new_s = make_good_string(n, s)

# Output the result
print(deleted)
print(new_s)
```
