
from collections import defaultdict
def solve(n, colors):
    pieces = defaultdict(list)
    for i, c in enumerate(colors, 1):
        pieces[c].append(i)
    
    for c in pieces:
        pieces[c] = sorted(pieces[c], reverse=True)
    
    res = []
    stack = []
    
    for i in range(n):
        c = colors[i]
        
        if not stack or stack[-1] != c:
            stack.append(c)
            res.append([i+1, i+1, c])
        else:
            stack.pop()
            
            if not stack:
                continue
            
            res.append([pieces[stack[-1]].pop(), i+1, stack[-1]])
            
    if stack:
        return "IMPOSSIBLE"
    
    return res
n = int(input())
colors = list(map(int, input().split()))
res = solve(n, colors)
if res == "IMPOSSIBLE":
    print(res)
else:
    print(len(res))
    for l, r, c in res:
        print(l, r, c)

