
def solve(A, B, C):
    if A == B:
        return C
    if A == C:
        return B
    return A

A, B, C = map(int, input().split())
print(solve(A, B, C))

