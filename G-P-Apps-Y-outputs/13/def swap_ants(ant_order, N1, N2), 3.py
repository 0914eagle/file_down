
def swap_ants(ant_order, N1, N2):
    new_order = ant_order[:]
    for i in range(N1-1):
        if ant_order[i] > ant_order[i+1]:
            new_order[i], new_order[i+1] = new_order[i+1], new_order[i]
    for i in range(N2-1, 0, -1):
        if ant_order[N1] < ant_order[i]:
            new_order[N1], new_order[i] = new_order[i], new_order[N1]
    return new_order

def find_final_order(N1, N2, order1, order2, T):
    ant_order = list(order1 + order2)
    for _ in range(T):
        ant_order = swap_ants(ant_order, N1, N2)
    return ''.join(ant_order)

N1, N2 = map(int, input().split())
order1 = input().strip()
order2 = input().strip()
T = int(input())

final_order = find_final_order(N1, N2, order1, order2, T)
print(final_order)
```
