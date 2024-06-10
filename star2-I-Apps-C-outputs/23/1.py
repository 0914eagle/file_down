
def solve(n, pairs):
    results = set()
    equations = []
    for a, b in pairs:
        if a + b not in results:
            equations.append((a, b, '+'))
            results.add(a + b)
        elif a - b not in results:
            equations.append((a, b, '-'))
            results.add(a - b)
        elif a * b not in results:
            equations.append((a, b, '*'))
            results.add(a * b)
        else:
            return "impossible"
    return equations

def main():
    n = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(n)]
    equations = solve(n, pairs)
    if equations == "impossible":
        print(equations)
    else:
        for a, b, op in equations:
            print(f"{a} {op} {b} = {eval(str(a) + op + str(b))}")

if __name__ == "__main__":
    main()

