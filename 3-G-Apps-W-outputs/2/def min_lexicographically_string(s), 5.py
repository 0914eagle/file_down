
def min_lexicographically_string(s):
    s = list(s)
    n = len(s)
    
    i = 0
    while i < n - 1:
        if s[i] == '0' and s[i+1] == '1':
            s[i], s[i+1] = s[i+1], s[i]
            i = max(0, i - 1)
        elif s[i] == '1' and s[i+1] == '2':
            s[i], s[i+1] = s[i+1], s[i]
            i = max(0, i - 1)
        else:
            i += 1
    
    return ''.join(s)

# Input
s = input().strip()

# Output
print(min_lexicographically_string(s))
