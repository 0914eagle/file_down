
import sys

def solve(k, a):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 3
    if k == 4:
        return 4
    if k == 5:
        return 5
    if k == 6:
        return 6
    if k == 7:
        return 7
    
    if a[0] == 1:
        return k
    
    if a[1] == 1:
        return k + 1
    
    if a[2] == 1:
        return k + 2
    
    if a[3] == 1:
        return k + 3
    
    if a[4] == 1:
        return k + 4
    
    if a[5] == 1:
        return k + 5
    
    if a[6] == 1:
        return k + 6
    
    return k + 7

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(k, a))

