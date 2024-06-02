
def min_lexicographically_string(s):
    s = list(s)
    n = len(s)
    
    for i in range(n-1):
        if s[i] > s[i+1]:
            if s[i] == '2' and s[i+1] == '0':
                s[i], s[i+1] = s[i+1], s[i]
            elif s[i] == '1' and s[i+1] == '0':
                s[i], s[i+1] = s[i+1], s[i]
            elif s[i] == '2' and s[i+1] == '1':
                s[i], s[i+1] = s[i+1], s[i]
            if i > 0:
                i -= 2
    
    return ''.join(s)

# Read input
s = input().strip()

# Call the function and print the result
print(min_lexicographically_string(s))
