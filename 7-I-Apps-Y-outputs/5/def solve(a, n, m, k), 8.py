


def solve(a, n, m, k):
    # write your code here
    max_sum = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] % k == 0:
                max_sum += a[i][j]
    return max_sum



