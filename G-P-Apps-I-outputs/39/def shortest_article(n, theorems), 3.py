
def shortest_article(n, theorems):
    memo = {}

    def dp(i, mask):
        if i == n:
            return 0
        
        if (i, mask) in memo:
            return memo[(i, mask)]

        ans = float('inf')
        for j in range(len(theorems[i])):
            length, num_deps, *deps = theorems[i][j]
            new_mask = mask
            for dep in deps:
                new_mask |= 1 << dep
            if new_mask == mask:  # No circular dependency
                ans = min(ans, length + dp(i+1, new_mask))

        memo[(i, mask)] = ans
        return ans

    return dp(0, 0)


# Input processing
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    theorems.append([list(map(int, input().split())) for _ in range(p)])

# Call the function and print the result
print(shortest_article(n, theorems))
```
