
def min_cost(n, a, b):
    if b < 2 * a:
        return n * a
    else:
        return n * b

q = int(input())
for _ in range(q):
    n, a, b = map(int, input().split())
    print(min_cost(n, a, b))

