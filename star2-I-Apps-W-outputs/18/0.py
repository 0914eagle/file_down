
def solve(n, m):
    if n == 1 or m == 1:
        return "Malvika"
    else:
        return "Akshat"

n, m = map(int, input().split())
print(solve(n, m))

