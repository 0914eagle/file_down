
def ant_jump(N1, N2, order1, order2, T):
    ants = list(order1 + order2)
    for _ in range(T):
        for i in range(len(ants) - 1):
            if (ants[i].isupper() and ants[i + 1].islower()) or (ants[i].islower() and ants[i + 1].isupper()):
                ants[i], ants[i + 1] = ants[i + 1], ants[i]
    return ''.join(ants)

# Input parsing
N1, N2 = map(int, input().split())
order1 = input().strip()
order2 = input().strip()
T = int(input().strip())

# Output
print(ant_jump(N1, N2, order1, order2, T))
```
