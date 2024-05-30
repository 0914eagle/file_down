
def find_shortest_article_length(n, theorems):
    dp = [0] * (1 << n)
    
    for i in range(n):
        for j in range(1 << n):
            length = theorems[i][0]
            dependencies = theorems[i][1:]
            
            if all(j & (1 << dep) for dep in dependencies):
                dp[j | (1 << i)] = max(dp[j | (1 << i)], dp[j] + length)
    
    return dp[(1 << n) - 1]

# Input parsing
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    dependencies = list(map(int, input().split()[1:]))
    theorems.append((p, dependencies))

# Find the shortest article length
shortest_length = find_shortest_article_length(n, theorems)
print(shortest_length)
```
