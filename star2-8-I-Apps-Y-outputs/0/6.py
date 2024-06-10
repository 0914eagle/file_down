
def solve(s):
    x = y = 0
    for c in s:
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y += 1
        else:
            y -= 1
    
    if x == 0 and y == 0:
        return (1, 2)
    
    l = r = 0
    for i, c in enumerate(s):
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y += 1
        else:
            y -= 1
        
        if x == 0 and y == 0:
            l = i + 1
            r = i + 1
            break
    
    if x != 0 or y != 0:
        return -1
    
    while r < len(s):
        if s[r] == 'L':
            x -= 1
        elif s[r] == 'R':
            x += 1
        elif s[r] == 'U':
            y += 1
        else:
            y -= 1
        
        if x == 0 and y == 0:
            return (l + 1, r + 1)
        
        r += 1
    
    return -1

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    
    l, r = solve(s)
    print(l, r)

