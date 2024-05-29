
def max_total_happiness(N, S, contestants):
    total_happiness = 0
    for contestant in contestants:
        required_slices = contestant[0]
        happiness_1 = contestant[1]
        happiness_2 = contestant[2]

        min_pizzas = (required_slices + S - 1) // S
        total_happiness += min_pizzas * min(happiness_1 * S, happiness_2 * S)

    return total_happiness

# Input reading
N, S = map(int, input().split())
contestants = []
for _ in range(N):
    s_i, a_i, b_i = map(int, input().split())
    contestants.append((s_i, a_i, b_i))

# Output
print(max_total_happiness(N, S, contestants))
```
