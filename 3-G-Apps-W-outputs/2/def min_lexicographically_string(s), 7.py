
def min_lexicographically_string(s):
    n = len(s)
    s = list(s)
    
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

# Read input
s = input().strip()

# Call the function and print the output
print(min_lexicographically_string(s))
