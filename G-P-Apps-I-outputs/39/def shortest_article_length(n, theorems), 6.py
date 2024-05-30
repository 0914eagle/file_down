
def shortest_article_length(n, theorems):
    def dfs(theorem_idx, memo):
        if theorem_idx in memo:
            return memo[theorem_idx]
        
        shortest_length = theorems[theorem_idx][0]
        for dependency in theorems[theorem_idx][2:]:
            shortest_length = max(shortest_length, theorems[theorem_idx][0] + dfs(dependency, memo))
        
        memo[theorem_idx] = shortest_length
        return shortest_length
    
    shortest_length = 0
    memo = {}
    for i in range(n):
        shortest_length = max(shortest_length, dfs(i, memo))
    
    return shortest_length

# Input parsing
n = int(input())
theorems = []
for _ in range(n):
    p, *theorem = map(int, input().split())
    theorems.append(theorem)

# Output
print(shortest_article_length(n, theorems))
```
