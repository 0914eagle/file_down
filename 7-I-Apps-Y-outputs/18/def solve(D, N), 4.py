
def solve(D, N):
    # Write your code here
    if D == 0:
        return 1
    elif D == 1:
        return 100
    elif D == 2:
        return 10000
    else:
        return 0

N = int(input())
D = int(input())
print(solve(D, N))

