
def ant_jump_order(N1, N2, ants1, ants2, T):
    ants1 = list(ants1)
    ants2 = list(ants2)
    
    for _ in range(T):
        for i in range(min(len(ants1), len(ants2))):
            if ants1[i] != ants2[i]:
                ants1[i], ants2[i] = ants2[i], ants1[i]
    
    return ''.join(ants1) + ''.join(ants2)

# Read input
N1, N2 = map(int, input().split())
ants1 = input().strip()
ants2 = input().strip()
T = int(input())

# Get and print the order of ants after T seconds
result = ant_jump_order(N1, N2, ants1, ants2, T)
print(result)
```
