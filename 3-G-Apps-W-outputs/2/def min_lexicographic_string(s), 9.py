
def min_lexicographic_string(s):
    n = len(s)
    s = list(s)
    
    i = 0
    while i < n:
        if s[i] == '0':
            s.remove('0')
            s.insert(0, '0')
        elif s[i] == '2':
            s.remove('2')
            s.append('2')
        else:
            i += 1
    
    return ''.join(s)

# Read input
s = input().strip()

# Output the result
print(min_lexicographic_string(s))
