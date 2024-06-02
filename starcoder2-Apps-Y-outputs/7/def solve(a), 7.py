
def solve(a):
    return sum(a) // len(a)

q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

