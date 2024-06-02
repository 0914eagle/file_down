
def solve(A, B, C):
    if A == B:
        return C
    elif A == C:
        return B
    else:
        return A

A, B, C = map(int, input().split())
print(solve(A, B, C))

