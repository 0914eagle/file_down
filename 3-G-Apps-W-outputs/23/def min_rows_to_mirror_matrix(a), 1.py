
def min_rows_to_mirror_matrix(a):
    n, m = len(a), len(a[0])
    
    for rows in range(n, 0, -1):
        if rows % 2 == 0:
            half_rows = rows // 2
            upper_half = a[:half_rows]
            lower_half = a[half_rows:rows]
            if upper_half == lower_half[::-1]:
                return rows
    
    return n

# Input processing
n, m = map(int, input().split())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

# Output
print(min_rows_to_mirror_matrix(a))
