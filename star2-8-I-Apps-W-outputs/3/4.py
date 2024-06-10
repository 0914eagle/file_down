
n, m = map(int, input().split())
table = [input() for _ in range(n)]

def good(table):
    for i in range(len(table)-1):
        if table[i] > table[i+1]:
            return False
    return True

ans = 0
for j in range(m):
    new_table = ["".join([row[i] for i in range(m) if i != j]) for row in table]
    if good(new_table):
        ans += 1

print(m - ans)

