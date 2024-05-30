
def swap_ants(ant_order1, ant_order2):
    return ant_order1[::-1] + ant_order2[::-1]

def jump_ants(N1, N2, ant_order1, ant_order2, T):
    for _ in range(T):
        new_order1 = ant_order1[:]
        new_order2 = ant_order2[:]
        for i in range(min(N1, N2) - 1):
            if ant_order1[i] != ant_order2[N2 - i - 1]:
                new_order1[i], new_order2[N2 - i - 1] = new_order2[N2 - i - 1], new_order1[i]
        ant_order1 = new_order1
        ant_order2 = new_order2
    return swap_ants(ant_order1, ant_order2)

N1, N2 = map(int, input().split())
ant_order1 = input().strip()
ant_order2 = input().strip()
T = int(input())

result = jump_ants(N1, N2, ant_order1, ant_order2, T)
print(result)
```
