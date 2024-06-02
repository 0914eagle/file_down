
def solve(K, S):
    return S[:K] + "..." if len(S) > K else S

K = int(input())
S = input()
print(solve(K, S))

