
import sys

def solve(N, M, k, s, p):
    # Complete this function
    pass

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    k = []
    s = []
    p = []
    for _ in range(N):
        k.append(int(input().strip()))
    for _ in range(M):
        s.append(list(map(int, input().strip().split())))
    for _ in range(M):
        p.append(int(input().strip()))
    result = solve(N, M, k, s, p)
    print(result)

