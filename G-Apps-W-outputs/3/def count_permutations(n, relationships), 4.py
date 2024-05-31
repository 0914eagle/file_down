
def count_permutations(n, relationships):
    dp = [[0] * (1 << (n - 1)) for _ in range(n)]
    
    for i in range(n):
        dp[i][1 << i] = 1
    
    for mask in range(1, 1 << (n - 1)):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if i == j or not (mask & (1 << j)) or relationships[j][i] == '0':
                    continue
                dp[i][mask] += dp[j][mask ^ (1 << i)]
    
    result = [0] * (1 << (n - 1))
    for mask in range(1 << (n - 1)):
        for i in range(n):
            result[mask] += dp[i][mask]
    
    return result

# Input
n = int(input())
relationships = [input() for _ in range(n)]

# Output
result = count_permutations(n, relationships)
print(*result)
