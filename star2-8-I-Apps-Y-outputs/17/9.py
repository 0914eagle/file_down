
m, n = map(int, input().split())
clauses = []
for _ in range(m):
    clauses.append(list(map(int, input().split())))
if m >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")

