
def max_total_happiness(N, S, contestants):
    total_happiness_type1 = sum(s * a for s, a, _ in contestants)
    total_happiness_type2 = sum(s * b for s, _, b in contestants)
    
    min_pizzas = (total_happiness_type1 + total_happiness_type2 - 1) // (S * 2)
    max_happiness = max(total_happiness_type1, total_happiness_type2)
    
    if min_pizzas == 0:
        return max_happiness
    
    remaining_slices = min_pizzas * S * 2
    sorted_contestants = sorted(contestants, key=lambda x: x[1] - x[2], reverse=True)
    
    idx = 0
    while remaining_slices > 0:
        s, a, b = sorted_contestants[idx]
        if a >= b:
            total_happiness_type1 += s * (a - b)
            remaining_slices -= s
        else:
            total_happiness_type2 += s * (b - a)
            remaining_slices -= s
        idx += 1
    
    return max(total_happiness_type1, total_happiness_type2)

# Input parsing
N, S = map(int, input().split())
contestants = []
for _ in range(N):
    s, a, b = map(int, input().split())
    contestants.append((s, a, b))

# Call the function and print the output
print(max_total_happiness(N, S, contestants))
```
