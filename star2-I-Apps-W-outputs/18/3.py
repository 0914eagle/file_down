
def solve(n, m):
    if (n * m) % 2 == 0:
        return "Malvika"
    else:
        return "Akshat"

n, m = map(int, input().split())
print(solve(n, m))

