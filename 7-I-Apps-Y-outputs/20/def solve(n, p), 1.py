
def solve(n, p):
    x = 0
    for i in range(len(p)):
        x += p[i]**(n[i])
    return x

n = int(input())
p = [int(input()) for _ in range(n)]
print(solve(list(map(int, input().split())), p))

