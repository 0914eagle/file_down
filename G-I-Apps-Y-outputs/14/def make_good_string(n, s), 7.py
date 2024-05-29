
def make_good_string(n, s):
    result = []
    for i in range(0, n, 2):
        if i+1 < n and s[i] == s[i+1]:
            result.append(i+1)
    
    chars_to_delete = len(result)
    new_string = ''.join([s[i] for i in range(n) if i not in result])
    
    return chars_to_delete, new_string

# Read input
n = int(input())
s = input()

# Solve the problem
chars_deleted, new_string = make_good_string(n, s)

# Print output
print(chars_deleted)
print(new_string)
```
