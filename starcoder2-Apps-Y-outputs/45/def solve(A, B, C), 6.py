
def solve(A, B, C):
    if A == B:
        return C
    elif B == C:
        return A
    else:
        return B

A, B, C = map(int, input().split())
print(solve(A, B, C))

