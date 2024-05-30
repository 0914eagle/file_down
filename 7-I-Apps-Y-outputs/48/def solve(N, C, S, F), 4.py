
import sys

def solve(N, C, S, F):
    # Write your code here
    for i in range(N-1):
        S[i+1] = S[i] + C[i]
        F[i+1] = F[i]
    for i in range(N-1, 0, -1):
        S[i] = S[i] - S[i] % F[i]
    return S

if __name__ == '__main__':
    N = int(input())
    C = [int(i) for i in input().split()]
    S = [int(i) for i in input().split()]
    F = [int(i) for i in input().split()]
    ans = solve(N, C, S, F)
    for i in range(N):
        print(ans[i])

