
def max_happiness(N, S, contestants):
    total_slices = sum(s for s, _, _ in contestants)
    
    pizzas = (total_slices + S - 1) // S  # Round up to nearest integer
    
    total_happiness_type1 = sum(s * a for s, a, _ in contestants)
    total_happiness_type2 = sum(s * b for s, _, b in contestants)
    
    return max(total_happiness_type1, total_happiness_type2) * pizzas

# Input parsing
N, S = map(int, input().split())
contestants = []
for _ in range(N):
    si, ai, bi = map(int, input().split())
    contestants.append((si, ai, bi))

# Calculate and print maximum total happiness
print(max_happiness(N, S, contestants))
```
