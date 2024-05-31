
def count_permutations(n, know_matrix):
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if know_matrix[i][j] == '1':
                adj_matrix[i][j] = 1

    dp = [[0 for _ in range(1 << (n-1))] for _ in range(n)]
    for i in range(1 << (n-1)):
        dp[0][i] = 1

    for i in range(1, n):
        for mask in range(1 << (n-1)):
            for j in range(n):
                if not adj_matrix[i][j]:
                    continue
                if (mask >> (j-1)) & 1:
                    dp[i][mask] += dp[i-1][mask ^ (1 << (j-1))]

    result = []
    for i in range(1 << (n-1)):
        result.append(dp[n-1][i])

    return result

# Reading input
n = int(input())
know_matrix = []
for _ in range(n):
    know_matrix.append(input())

# Solving the problem
result = count_permutations(n, know_matrix)

# Printing the output
print(*result)
