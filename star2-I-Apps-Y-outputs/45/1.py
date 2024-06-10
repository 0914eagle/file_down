
def solve(n, a, b):
    if a < 2*b:
        return n*a
    else:
        return (n//2)*2*b + (n%2)*a

q = int(input())
for _ in range(q):
    n, a, b = map(int, input().split())
    print(solve(n, a, b))

