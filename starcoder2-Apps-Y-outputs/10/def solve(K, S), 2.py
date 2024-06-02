
def solve(K, S):
    if len(S) <= K:
        return S
    else:
        return S[:K] + "..."

K = int(input())
S = input()
print(solve(K, S))

