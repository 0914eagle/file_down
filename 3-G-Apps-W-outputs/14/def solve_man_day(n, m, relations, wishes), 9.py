
def solve_man_day(n, m, relations, wishes):
    ancestors = {}
    for p, q in relations:
        if q not in ancestors:
            ancestors[q] = []
        ancestors[q].append(p)

    candidates = []
    for i in range(n):
        if i + 1 in ancestors:
            if wishes[i] in ancestors[i + 1]:
                candidates.append(i + 1)
            else:
                return -1

    return candidates

# Input parsing
n, m = map(int, input().split())
relations = [tuple(map(int, input().split())) for _ in range(m)]
wishes = list(map(int, input().split()))

result = solve_man_day(n, m, relations, wishes)
if result == -1:
    print(-1)
else:
    print(len(result))
    for man in result:
        print(man)
