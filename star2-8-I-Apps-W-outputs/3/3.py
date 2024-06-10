
def isGood(table):
    for i in range(len(table)-1):
        if table[i] > table[i+1]:
            return False
    return True

def solve(table):
    n = len(table)
    m = len(table[0])
    for j in range(m):
        table_new = ["".join([table[i][k] for k in range(m) if k != j]) for i in range(n)]
        if isGood(table_new):
            return j
    return m

n, m = map(int, input().split())
table = []
for i in range(n):
    table.append(input())

print(solve(table))

