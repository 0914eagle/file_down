
import sys

def solve(n, m, edges):
    g = [[] for i in range(n)]
    for a, b in edges:
        g[a-1].append(b-1)
    
    in_out = [0] * n
    
    for i in range(n):
        for j in g[i]:
            in_out[i] += 1
            in_out[j] -= 1
    
    res = 0
    
    for i in range(n):
        if in_out[i] == 0:
            res += 1
    
    return res, in_out
    
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    edges = [tuple(map(int, sys.stdin.readline().strip().split())) for i in range(m)]
    
    res, in_out = solve(n, m, edges)
    
    print(res)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if in_out[i] > 0 and in_out[j] < 0:
                print(i+1, j+1)
                in_out[i] -= 1
                in_out[j] += 1
            

