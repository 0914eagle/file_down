
def count_permutations(n, connections):
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if connections[i][j] == '1':
                adj_matrix[i][j] = 1
    
    dp = [[0 for _ in range(1 << (n-1))] for _ in range(n)]
    dp[0][0] = 1
    
    for mask in range(1 << (n-1)):
        for i in range(1, n):
            if (mask & (1 << (i-1))) == 0:
                continue
            for j in range(n):
                if j == i or adj_matrix[i][j] == 0:
                    continue
                dp[i][mask] += dp[j][mask ^ (1 << (i-1))]
    
    ans = [0] * (1 << (n-1))
    for mask in range(1 << (n-1)):
        for i in range(n):
            ans[mask] += dp[i][mask]
    
    return ans

# Input
n = int(input())
connections = [input() for _ in range(n)]

# Solve
output = count_permutations(n, connections)

# Output
print(" ".join(map(str, output)))
