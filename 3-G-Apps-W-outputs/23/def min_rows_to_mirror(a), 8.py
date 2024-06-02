
def min_rows_to_mirror(a):
    n, m = len(a), len(a[0])
    for rows in range(1, n + 1):
        if n % rows == 0:
            valid = True
            for i in range(rows // 2):
                if a[i] != a[rows - 1 - i]:
                    valid = False
                    break
            if valid:
                return rows
    return n

# Input
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Output
print(min_rows_to_mirror(a))
