
def solve(n, a):
    return sum(a) // n

q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

