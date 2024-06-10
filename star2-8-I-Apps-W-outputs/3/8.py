
def is_good(table):
    n = len(table)
    if n == 0:
        return True
    prev = table[0]
    for row in table[1:]:
        if row < prev:
            return False
        prev = row
    return True


def min_ops(table):
    n, m = len(table), len(table[0])
    for j in range(m):
        new_table = [row[:j] + row[j + 1:] for row in table]
        if is_good(new_table):
            return 1
    return m


n, m = map(int, input().split())
table = [input() for _ in range(n)]
print(min_ops(table))

