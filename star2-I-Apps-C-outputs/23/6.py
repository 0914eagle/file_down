
def solve(n, pairs):
    results = set()
    for a, b in pairs:
        for op in ['+', '-', '*']:
            result = eval(f"{a} {op} {b}")
            if result not in results:
                results.add(result)
                yield f"{a} {op} {b} = {result}"
                break
        else:
            yield "impossible"

n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
for answer in solve(n, pairs):
    print(answer)

