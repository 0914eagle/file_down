
def shortest_article_length():
    n = int(input())
    proofs = {}
    for i in range(n):
        p = int(input())
        proof_lengths = []
        for _ in range(p):
            l, k, *dependencies = map(int, input().split())
            proof_lengths.append((l, dependencies))
        proofs[i] = proof_lengths

    dp = [[0] * (1 << n) for _ in range(n)]

    def solve(curr_theorem, bitmask):
        if bitmask == (1 << n) - 1:
            return 0
        if dp[curr_theorem][bitmask] != 0:
            return dp[curr_theorem][bitmask]

        min_length = float('inf')
        for length, dependencies in proofs[curr_theorem]:
            depends_on = 0
            for dependency in dependencies:
                depends_on |= 1 << dependency
            if (depends_on & bitmask) == depends_on:
                min_length = min(min_length, length + solve(curr_theorem, bitmask | (1 << curr_theorem)))

        dp[curr_theorem][bitmask] = min_length
        return min_length

    result = float('inf')
    for i in range(n):
        result = min(result, solve(i, 1 << i))
    
    return result

print(shortest_article_length())
```
