
def min_sum_visible_fields(N, K, table):
    rows = [sum(row) for row in table]
    cols = [sum(col) for col in zip(*table)]
    
    row_pairs = []
    for i in range(N-1):
        row_pairs.append((rows[i], rows[i+1]))
    
    col_pairs = []
    for i in range(N-1):
        col_pairs.append((cols[i], cols[i+1]))
    
    visible_sums = []
    for k in range(K+1):
        visible_sum = sum(rows) # sum of all fields initially
        for i in range(N-1):
            if k & 1: # check if k-th bit is set
                visible_sum -= min(row_pairs[i])
            else:
                visible_sum -= max(row_pairs[i])
        for i in range(N-1):
            if k & 2: # check if (k-1)-th bit is set
                visible_sum -= min(col_pairs[i])
            else:
                visible_sum -= max(col_pairs[i])
        visible_sums.append(visible_sum)
    
    return min(visible_sums)

# Read input
N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# Output the minimal sum of visible fields
print(min_sum_visible_fields(N, K, table))
