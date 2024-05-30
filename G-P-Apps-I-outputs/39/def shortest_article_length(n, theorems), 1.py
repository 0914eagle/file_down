
def shortest_article_length(n, theorems):
    memo = {}

    def dp(i, mask):
        if i == n:
            return 0

        if (i, mask) in memo:
            return memo[(i, mask)]

        ans = float('inf')
        for j in range(len(theorems[i])):
            length, _, *dependencies = theorems[i][j]
            new_mask = mask
            for dep in dependencies:
                new_mask |= 1 << dep
            ans = min(ans, length + dp(i + 1, new_mask))

        memo[(i, mask)] = ans
        return ans

    return dp(0, 0)

# Input parsing
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    theorem = []
    for _ in range(p):
        p_info = list(map(int, input().split()))
        theorem.append(p_info)
    theorems.append(theorem)

result = shortest_article_length(n, theorems)
print(result)
```
