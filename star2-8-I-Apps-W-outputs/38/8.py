
n = int(input())

def solve(n):
    if n == 1:
        return 2
    else:
        return solve(n - 1) * 2

print(solve(n))

