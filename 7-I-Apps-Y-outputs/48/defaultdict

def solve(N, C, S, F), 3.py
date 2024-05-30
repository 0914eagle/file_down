
from collections import defaultdict

def solve(N, C, S, F):
    d = defaultdict(int)
    for i in range(1, N):
        d[i] = d[i - 1] + S[i - 1]
    ans = [0] * N
    for i in range(1, N):
        ans[i] = d[i - 1] + S[i - 1]
        if ans[i] % F[i] != 0:
            ans[i] += F[i] - ans[i] % F[i]
    for i in range(N - 1, 0, -1):
        ans[i - 1] = max(ans[i - 1], ans[i] + C[i - 1])
    return ans

if __name__ == "__main__":
    N = int(input())
    C = []
    S = []
    F = []
    for i in range(N - 1):
        C.append(int(input()))
        S.append(int(input()))
        F.append(int(input()))
    ans = solve(N, C, S, F)
    for i in range(N):
        print(ans[i])

