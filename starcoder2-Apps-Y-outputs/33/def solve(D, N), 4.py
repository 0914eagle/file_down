
def solve(D, N):
    if D == 0:
        return N
    if D == 1:
        return 100*N
    if D == 2:
        return 10000*N

D, N = map(int, input().split())
print(solve(D, N))

