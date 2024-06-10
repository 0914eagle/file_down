
def solve(n, m, volcanoes):
    pass

n, m = map(int, input().split())
volcanoes = set()
for _ in range(m):
    x, y = map(int, input().split())
    volcanoes.add((x, y))

print(solve(n, m, volcanoes))

