
def max_total_happiness(N, S, contestants):
    total_happiness_type1 = sum(s * a for s, a, _ in contestants)
    total_happiness_type2 = sum(s * b for s, _, b in contestants)
    
    min_pizzas_needed = (total_happiness_type1 + total_happiness_type2 - 1) // (S)
    
    return min_pizzas_needed * S

# Input parsing
N, S = map(int, input().split())
contestants = [tuple(map(int, input().split())) for _ in range(N)]

# Output the result
print(max_total_happiness(N, S, contestants))
