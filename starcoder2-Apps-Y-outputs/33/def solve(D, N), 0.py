
def solve(D, N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    else:
        return N * 10000

D, N = map(int, input().split())
print(solve(D, N))

