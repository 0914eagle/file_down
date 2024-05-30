
def swap_ants(ants1, ants2):
    new_ants1 = ants1[:]
    new_ants2 = ants2[:]
    for idx in range(len(ants1) - 1):
        if ants1[idx] in new_ants1 and ants1[idx+1] in new_ants2:
            new_ants1[idx], new_ants1[idx+1] = new_ants1[idx+1], new_ants1[idx]
        if ants2[idx] in new_ants2 and ants2[idx+1] in new_ants1:
            new_ants2[idx], new_ants2[idx+1] = new_ants2[idx+1], new_ants2[idx]
    return new_ants1, new_ants2

def find_order_after_T_seconds(N1, N2, ants1, ants2, T):
    for _ in range(T):
        ants1, ants2 = swap_ants(ants1, ants2)
    return "".join(ants1) + "".join(ants2)

# Input parsing
N1, N2 = map(int, input().split())
ants1 = list(input().strip())
ants2 = list(input().strip())
T = int(input())

print(find_order_after_T_seconds(N1, N2, ants1, ants2, T))
```
