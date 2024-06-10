
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    
    res = 1
    for i in range(1, N+1):
        res = res * pow(i, M, 10**9+7) % (10**9+7)
    
    print(res)

solve()

