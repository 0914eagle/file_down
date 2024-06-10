
def solve(n, dist):
    pass

n = int(input())
dist = []
for i in range(n - 1):
    dist.append(list(map(int, input().split())))
print(solve(n, dist))

