
def shortest_article_length(n, theorems):
    dp = [0] * (1 << n)
    
    for i in range(n):
        proofs = theorems[i]
        for proof in proofs:
            mask = 0
            for d in proof[2:]:
                mask |= 1 << d
            for j in range(1, 1 << n):
                if j & mask == mask:
                    dp[j] = max(dp[j], dp[j ^ mask] + proof[0])
    
    return dp[(1 << n) - 1]

# Reading input
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proofs = []
    for _ in range(p):
        proof = list(map(int, input().split()))
        proofs.append(proof)
    theorems.append(proofs)

# Calculate and print the shortest possible length of David's article
print(shortest_article_length(n, theorems))
```
