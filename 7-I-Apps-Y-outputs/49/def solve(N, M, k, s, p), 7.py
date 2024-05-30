
import sys

def solve(N, M, k, s, p):
    # Complete this function
    return 0

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    k = [0] * M
    s = []
    p = []
    for i in range(M):
        s.append(list(map(int, input().strip().split())))
    for i in range(M):
        p.append(int(input().strip()))
    result = solve(N, M, k, s, p)
    print(result)

