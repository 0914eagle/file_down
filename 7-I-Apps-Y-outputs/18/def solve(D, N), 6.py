

def solve(D, N):
    if D == 0:
        return N * 100
    elif D == 1:
        return N * 100 + 1
    elif D == 2:
        return N * 100 + 2

print(solve(int(input().split()[0]), int(input())))

