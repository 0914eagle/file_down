
def solve(n, pairs):
    results = set()
    for a, b in pairs:
        if a + b not in results:
            results.add(a + b)
            yield f"{a} + {b} = {a + b}"
        elif a - b not in results:
            results.add(a - b)
            yield f"{a} - {b} = {a - b}"
        elif a * b not in results:
            results.add(a * b)
            yield f"{a} * {b} = {a * b}"
        else:
            yield "impossible"

n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
for answer in solve(n, pairs):
    print(answer)

