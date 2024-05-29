
def max_total_happiness(N, S, contestants):
    total_happiness = 0
    max_a = max([c[1] for c in contestants])
    max_b = max([c[2] for c in contestants])
    
    for i in range(N):
        slices_needed = contestants[i][0]
        a_happiness = contestants[i][1]
        b_happiness = contestants[i][2]
        
        max_happiness = max(a_happiness, b_happiness)
        
        extra_slices = slices_needed % S
        pizzas_needed = slices_needed // S if extra_slices == 0 else slices_needed // S + 1
        
        total_happiness += pizzas_needed * max_happiness
    
    return total_happiness

# Reading input
N, S = map(int, input().split())
contestants = []
for _ in range(N):
    s, a, b = map(int, input().split())
    contestants.append((s, a, b))

# Output
print(max_total_happiness(N, S, contestants))
