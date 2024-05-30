
def shortest_article_length(n, theorems):
    dp = [[0] * (n + 1) for _ in range(1 << n)]
    
    for i, theorem in enumerate(theorems):
        for j in range(1 << n):
            if j & (1 << i):
                continue
            new_j = j | (1 << i)
            for l, k, *d in theorem:
                new_dp = dp[j][i] + l
                for dep in d:
                    if not j & (1 << dep):
                        new_dp = -1
                        break
                    new_dp += dp[j][dep]
                if new_dp != -1 and new_dp < dp[new_j][i]:
                    dp[new_j][i] = new_dp
    
    return min(dp[-1])

# Input parsing
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    theorem = []
    for _ in range(p):
        l, k, *d = map(int, input().split())
        theorem.append((l, k, d))
    theorems.append(theorem)

# Call the function and print the output
print(shortest_article_length(n, theorems))
```
