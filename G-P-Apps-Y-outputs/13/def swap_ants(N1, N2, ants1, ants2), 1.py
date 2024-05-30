
def swap_ants(N1, N2, ants1, ants2):
    for _ in range(T):
        new_ants1 = [''] * N1
        new_ants2 = [''] * N2

        for i in range(N1):
            if i == 0:
                new_ants1[i] = ants1[i]
            elif ants1[i] != ants2[N2 - 1]:
                new_ants1[i] = ants1[i-1]
            else:
                new_ants1[i] = ants2[N2 - 1]

        for i in range(N2):
            if i == N2 - 1:
                new_ants2[i] = ants2[i]
            elif ants2[i] != ants1[0]:
                new_ants2[i] = ants2[i+1]
            else:
                new_ants2[i] = ants1[0]

        ants1 = new_ants1
        ants2 = new_ants2

    return ''.join(new_ants1) + ''.join(new_ants2)

# Input processing
N1, N2 = map(int, input().split())
ants1 = list(input().strip())
ants2 = list(input().strip())
T = int(input())

print(swap_ants(N1, N2, ants1, ants2))
```
