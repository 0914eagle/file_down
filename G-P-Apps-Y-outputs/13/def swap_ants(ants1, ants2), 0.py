
def swap_ants(ants1, ants2):
    i = 0
    while i < len(ants1) - 1 and i < len(ants2) - 1:
        if ants1[i] < ants2[i] and ants1[i+1] > ants2[i+1]:
            ants1[i], ants2[i] = ants2[i], ants1[i]
        i += 1
    return ants1 + ants2

def ant_swap_order(N1, N2, ants1, ants2, T):
    for _ in range(T):
        ants1 = list(ants1)
        ants2 = list(ants2)
        ants = swap_ants(ants1, ants2)
        ants1 = ''.join(ants[:N1])
        ants2 = ''.join(ants[N1:])
    return ants1 + ants2

N1, N2 = map(int, input().split())
ants1 = input().strip()
ants2 = input().strip()
T = int(input())

result = ant_swap_order(N1, N2, ants1, ants2, T)
print(result)
```
