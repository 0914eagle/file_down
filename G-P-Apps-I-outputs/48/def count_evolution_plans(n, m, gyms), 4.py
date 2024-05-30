
MOD = 10**9 + 7

def count_evolution_plans(n, m, gyms):
    counts = [0] * (m + 1)
    for g in gyms:
        for t in g[1:]:
            counts[t] += 1

    counts.sort()
    ans = 1
    for i in range(1, m + 1):
        ans = (ans * (counts[i] - counts[i - 1])) % MOD

    return ans

# Input parsing
n, m = map(int, input().split())
gyms = []
for _ in range(n):
    g = list(map(int, input().split()))[1:]
    gyms.append(g)

# Output the result
print(count_evolution_plans(n, m, gyms))
```
