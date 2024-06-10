
def solve(n, pairs):
    results = set()
    for a, b in pairs:
        if a + b not in results:
            yield f"{a} + {b} = {a + b}"
            results.add(a + b)
        elif a - b not in results:
            yield f"{a} - {b} = {a - b}"
            results.add(a - b)
        elif a * b not in results:
            yield f"{a} * {b} = {a * b}"
            results.add(a * b)
        else:
            yield "impossible"

n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
for equation in solve(n, pairs):
    print(equation)

