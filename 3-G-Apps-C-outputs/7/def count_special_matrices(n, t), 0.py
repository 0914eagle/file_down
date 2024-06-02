
def count_special_matrices(n, t):
    count = 0
    for m in range(1, n+1):
        if (m + 1) ^ m == t:
            count += 1
    return count

n, t = map(int, input().split())
result = count_special_matrices(n, t)
print(result)
