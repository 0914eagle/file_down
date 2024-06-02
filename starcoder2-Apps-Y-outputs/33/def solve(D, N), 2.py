
def solve(D, N):
    if D == 0:
        return N
    elif D == 1:
        return 100 * N
    else:
        return 10000 * N

D, N = map(int, input().split())
print(solve(D, N))

