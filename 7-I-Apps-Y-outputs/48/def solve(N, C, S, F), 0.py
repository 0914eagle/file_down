
import sys

def solve(N, C, S, F):
    if N == 1:
        return S[0]
    else:
        return S[0] + solve(N-1, C[:-1], S[1:], F[:-1])

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    C = []
    S = []
    F = []
    for i in range(N-1):
        C.append(int(sys.stdin.readline()))
        S.append(int(sys.stdin.readline()))
        F.append(int(sys.stdin.readline()))
    print(solve(N, C, S, F))

