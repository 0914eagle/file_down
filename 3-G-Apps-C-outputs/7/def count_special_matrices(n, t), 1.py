
def count_special_matrices(n, t):
    count = 0
    for m in range(1, n + 1):
        row_sum = 0
        for j in range(1, m + 2):
            row_sum ^= (m + 1 + j)
        if row_sum == t:
            count += 1
    return count

n, t = map(int, input().split())
result = count_special_matrices(n, t)
print(result)
