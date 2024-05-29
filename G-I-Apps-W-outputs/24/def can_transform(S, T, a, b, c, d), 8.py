
def can_transform(S, T, a, b, c, d):
    def helper(source, target):
        if not target:
            return True
        if not source:
            return False
        
        if source[0] == target[0]:
            return helper(source[1:], target[1:])
        if source[0] == 'A' and (target[0] == 'B' or target[0] == 'C'):
            return helper(source[1:], target)
        elif source[0] == 'B' and (target[0] == 'A' or target[0] == 'C'):
            return helper(source[1:], target)
        elif source[0] == 'C' and (target[0] == 'A' or target[0] == 'B'):
            return helper(source[1:], target)
        elif source[:3] == 'AAA':
            return helper(source[3:], target)
        return False
    
    result = []
    for i in range(len(a)):
        sub_S = S[a[i]-1:b[i]]  # substring S[a[i]..b[i]]
        sub_T = T[c[i]-1:d[i]]  # substring T[c[i]..d[i]]
        
        if len(sub_S) < len(sub_T):
            result.append('0')
        else:
            result.append('1' if helper(sub_S, sub_T) else '0')
    
    return ''.join(result)

# Reading input
S = input().strip()
T = input().strip()
Q = int(input().strip())
a, b, c, d = [], [], [], []
for _ in range(Q):
    inp = input().strip().split()
    a.append(int(inp[0]))
    b.append(int(inp[1]))
    c.append(int(inp[2]))
    d.append(int(inp[3]))

# Output
print(can_transform(S, T, a, b, c, d))
```
