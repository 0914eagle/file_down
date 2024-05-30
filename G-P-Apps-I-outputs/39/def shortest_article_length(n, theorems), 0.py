
def shortest_article_length(n, theorems):
    memo = {}

    def dp(idx, mask):
        if idx == n:
            return 0
        if (idx, mask) in memo:
            return memo[(idx, mask)]

        ans = float('inf')
        for i in range(len(theorems[idx])):
            length, num_deps, *deps = theorems[idx][i]
            new_mask = mask
            for dep in deps:
                new_mask |= 1 << dep
            if new_mask == mask:  # current theorem doesn't depend on any other theorems
                ans = min(ans, length + dp(idx + 1, mask))
            else:
                ans = min(ans, length + dp(idx + 1, new_mask))
        
        memo[(idx, mask)] = ans
        return ans

    return dp(0, 0)

# Input parsing
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    theorem = []
    for _ in range(p):
        proof = list(map(int, input().split()))
        theorem.append(proof)
    theorems.append(theorem)

# Call the function and output the result
print(shortest_article_length(n, theorems))
```
