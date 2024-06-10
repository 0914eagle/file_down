
import sys

def min_button_push(f, s, g, u, d):
    dist = [sys.maxsize] * (f+1)
    dist[s] = 0
    
    for i in range(s, f+1):
        if i + u <= f:
            if dist[i+u] > dist[i] + 1:
                dist[i+u] = dist[i] + 1
        if i - d >= 1:
            if dist[i-d] > dist[i] + 1:
                dist[i-d] = dist[i] + 1
    
    if dist[g] == sys.maxsize:
        return "use the stairs"
    
    return dist[g]
f, s, g, u, d = [int(x) for x in input().split()]
print(min_button_push(f, s, g, u, d))

