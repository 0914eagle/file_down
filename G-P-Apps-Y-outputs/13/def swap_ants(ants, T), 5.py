
def swap_ants(ants, T):
    for _ in range(T):
        i = 0
        while i < len(ants) - 1:
            if (ants[i].isupper() and ants[i+1].islower()) or (ants[i].islower() and ants[i+1].isupper()):
                ants[i], ants[i+1] = ants[i+1], ants[i]
                i += 2
            else:
                i += 1
    return "".join(ants)

# Input
N1, N2 = map(int, input().split())
ants_row1 = list(input().strip())
ants_row2 = list(input().strip())
T = int(input())

# Combine ants from both rows
ants = ants_row1 + ants_row2

# Calculate final order of ants after T seconds
final_order = swap_ants(ants, T)

# Output
print(final_order)
```
