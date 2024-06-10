
def solve(t, s):
    n, m = len(t), len(s)
    pos = [[] for _ in range(26)]
    for i, (l, c) in enumerate(t):
        pos[ord(c) - ord('a')].append(i)
    
    res = 0
    for i, (l, c) in enumerate(s):
        idx = ord(c) - ord('a')
        if not pos[idx]:
            return 0
        
        j = bisect.bisect_left(pos[idx], i)
        if j == len(pos[idx]):
            return 0
        
        i = pos[idx][j]
        if i + l > n:
            return 0
        
        if t[i:i+l] != s[i:i+l]:
            return 0
        
        res += 1
    
    return res

