
N, M = map(int, input().split())
houses = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    houses[a] = 1
    houses[b] = 1
if sum(houses) == N:
    print("Connected")
else:
    for i in range(1, N+1):
        if houses[i] == 0:
            print(i)
