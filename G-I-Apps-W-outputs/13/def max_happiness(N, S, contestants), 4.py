
def max_happiness(N, S, contestants):
    min_slices = min(contestants, key=lambda x: min(x[1], x[2]))
    
    type1_happiness = sum(min_slices[1] * min_slices[0])
    type2_happiness = sum(min_slices[2] * min_slices[0])
    
    return max(type1_happiness, type2_happiness) * (N // S) + max(type1_happiness, type2_happiness) * (N % S)

# Input
N, S = map(int, input().split())
contestants = []
for _ in range(N):
    s, a, b = map(int, input().split())
    contestants.append((s, a, b))

# Output
print(max_happiness(N, S, contestants))
