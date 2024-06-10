
def solve(n, m):
    if (n * m) % 2 == 1:
        return "Akshat"
    else:
        return "Malvika"

n, m = map(int, input().split())
print(solve(n, m))

