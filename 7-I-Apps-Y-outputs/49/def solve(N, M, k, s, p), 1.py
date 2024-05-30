
import sys

def solve(N, M, k, s, p):
    # Write your code here
    pass

if __name__ == "__main__":
    N, M = map(int, input().split())
    k = [list(map(int, input().split())) for _ in range(M)]
    s = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    print(solve(N, M, k, s, p))

