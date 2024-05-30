
def shortest_article_length(n, theorems):
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for i in range(1 << n):
        for j in range(n):
            if (i & (1 << j)) == 0:
                cur_len = 0
                for proof in theorems[j]:
                    l, k, d = proof
                    if all((i & (1 << dep)) != 0 for dep in d):
                        cur_len = max(cur_len, l)
                dp[i | (1 << j)] = min(dp[i | (1 << j)], dp[i] + cur_len)

    return dp[(1 << n) - 1]

n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proofs = []
    for _ in range(p):
        l, k, *d = map(int, input().split())
        proofs.append((l, k, d))
    theorems.append(proofs)

print(shortest_article_length(n, theorems))
```
