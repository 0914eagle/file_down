
def max_total_happiness(N, S, contestants):
    total_slices = sum(s for s, _, _ in contestants)
    total_happiness = 0
    
    for s, a, b in contestants:
        total_happiness += max(a, b) * s
    
    pizzas_needed = (total_slices + S - 1) // S
    return total_happiness // pizzas_needed

# Input parsing
N, S = map(int, input().split())
contestants = []
for _ in range(N):
    s, a, b = map(int, input().split())
    contestants.append((s, a, b))

# Call the function and print the output
print(max_total_happiness(N, S, contestants))
```
