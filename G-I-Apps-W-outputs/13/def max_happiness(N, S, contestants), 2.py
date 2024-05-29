
def max_happiness(N, S, contestants):
    total_happiness = 0

    type1_slices_needed = sum(s for s, _, _ in contestants)
    type2_slices_needed = sum(s for s, _, _ in contestants)

    for s, a, b in contestants:
        if a > b:
            type1_slices_needed -= s
            total_happiness += s * a
        else:
            type2_slices_needed -= s
            total_happiness += s * b

    pizzas_needed = -(-type1_slices_needed // S) + -(-type2_slices_needed // S)

    return total_happiness, pizzas_needed


# Input parsing
N, S = map(int, input().split())
contestants = [list(map(int, input().split())) for _ in range(N)]

happiness, pizzas = max_happiness(N, S, contestants)
print(happiness)
