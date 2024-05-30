
def shortest_article_length(n, theorems):
    dp = [0] * (1 << n)
    
    for i in range(1, 1 << n):
        dp[i] = float('inf')
        for j in range(n):
            if i & (1 << j):
                prev_proof = dp[i ^ (1 << j)]
                for proof_length, _, dependencies in theorems[j]:
                    if all(k in bin(i)[:1:-1] for k in dependencies):
                        dp[i] = min(dp[i], prev_proof + proof_length)
    
    return dp[(1 << n) - 1]

if __name__ == "__main__":
    n = int(input())
    theorems = []
    for _ in range(n):
        p = int(input())
        proofs = []
        for _ in range(p):
            length, k, *dependencies = map(int, input().split())
            proofs.append((length, k, dependencies))
        theorems.append(proofs)
    
    result = shortest_article_length(n, theorems)
    print(result)
```
