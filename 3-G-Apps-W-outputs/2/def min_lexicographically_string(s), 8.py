
def min_lexicographically_string(s):
    n = len(s)
    s = list(s)
    
    for i in range(n-1):
        if s[i] > s[i+1]:
            if s[i] == '1' and s[i+1] == '0':
                s[i], s[i+1] = s[i+1], s[i]
            elif s[i] == '2' and s[i+1] == '1':
                s[i], s[i+1] = s[i+1], s[i]
            else:
                for j in range(i+2, n):
                    if s[j] == '0' and s[i] == '1':
                        s[i], s[j] = s[j], s[i]
                        break
                    elif s[j] == '1' and s[i] == '2':
                        s[i], s[j] = s[j], s[i]
                        break
    
    return ''.join(s)

# Read input
s = input().strip()

# Output the result
print(min_lexicographically_string(s))
