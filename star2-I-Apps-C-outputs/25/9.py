
def solve(n, m, volcanoes):
    pass

n, m = map(int, input().split())
volcanoes = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, m, volcanoes))

