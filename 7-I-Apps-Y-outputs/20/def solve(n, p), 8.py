
def solve(n, p):
    return sum(int(p[i]) ** int(p[i + 1]) for i in range(0, len(p), 2))

n = int(input())
p = [input() for _ in range(n)]
print(solve(n, p))

