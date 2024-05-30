
def swap_ants(order1, order2, t):
    ant_order = list(order1 + order2)
    for _ in range(t):
        for i in range(len(ant_order) - 1):
            if i < len(order1) and i + 1 >= len(order1):
                ant_order[i], ant_order[i + 1] = ant_order[i + 1], ant_order[i]
            elif i >= len(order1) and i + 1 < len(order1):
                ant_order[i], ant_order[i + 1] = ant_order[i + 1], ant_order[i]
    return ''.join(ant_order)

# Input processing
N1, N2 = map(int, input().split())
order1 = input().strip()
order2 = input().strip()
T = int(input())

# Output
print(swap_ants(order1, order2, T))
```
