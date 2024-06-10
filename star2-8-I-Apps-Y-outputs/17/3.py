
def solve(m, n, clauses):
    if m >= 8:
        return "satisfactory"
    return "unsatisfactory"

m, n = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(m)]
print(solve(m, n, clauses))

