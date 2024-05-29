
def max_happiness(N, S, contestants):
    total_happiness_1 = sum(s * a for s, a, _ in contestants)
    total_happiness_2 = sum(s * b for s, _, b in contestants)
    
    min_pizzas = (total_happiness_1 + total_happiness_2 + S - 1) // S
    max_happiness = max(total_happiness_1, total_happiness_2) * min_pizzas

    return max_happiness

# Input
N, S = map(int, input().split())
contestants = [tuple(map(int, input().split())) for _ in range(N)]

# Output
print(max_happiness(N, S, contestants))
