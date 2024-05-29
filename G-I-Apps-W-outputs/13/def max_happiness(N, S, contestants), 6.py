
def max_happiness(N, S, contestants):
    happiness_type1 = sum(s * a for s, a, _ in contestants)
    happiness_type2 = sum(s * b for s, _, b in contestants)
    return max(happiness_type1, happiness_type2)

# Input parsing
N, S = map(int, input().split())
contestants = []
for _ in range(N):
    s, a, b = map(int, input().split())
    contestants.append((s, a, b))

# Output
print(max_happiness(N, S, contestants))
```
