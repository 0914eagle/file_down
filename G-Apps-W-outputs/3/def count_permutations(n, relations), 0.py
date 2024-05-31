
def count_permutations(n, relations):
    adj_matrix = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if relations[i][j] == '1':
                adj_matrix[i][j] = True

    dp = [0] * (1 << (n-1))
    for mask in range(1, 1 << (n-1)):
        s = [0] * (n-1)
        for i in range(n-1):
            s[i] = (mask >> i) & 1
        
        valid = True
        for i in range(n-1):
            for j in range(i+1, n-1):
                if (s[i] and s[j]) and not adj_matrix[i][j]:
                    valid = False
                    break
                if (not s[i] and not s[j]) and adj_matrix[i][j]:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            dp[mask] = 1
    
    for i in range(n-1):
        for mask in range(1, 1 << (n-1)):
            if mask & (1 << i):
                dp[mask] += dp[mask ^ (1 << i)]
    
    return dp


n = int(input())
relations = [input() for _ in range(n)]

result = count_permutations(n, relations)
print(' '.join(map(str, result)))
