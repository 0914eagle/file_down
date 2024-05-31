
def frog_energy(N, K, plants):
    energy = [0] * N
    jumps = [0] * N
    prev = [-1] * N

    for i in range(1, N):
        energy[i] = plants[i][2]
        for j in range(i):
            cost = max(abs(plants[i][0] - plants[j][0]), abs(plants[i][1] - plants[j][1])) * K
            if energy[i] < energy[j] - cost + plants[i][2]:
                energy[i] = energy[j] - cost + plants[i][2]
                prev[i] = j
                jumps[i] = jumps[j] + 1

    path = []
    current = N - 1
    while current != -1:
        path.append(current)
        current = prev[current]

    path.reverse()
    return energy[N-1], len(path), [p + 1 for p in path]

# Input processing
N, K = map(int, input().split())
plants = []
for _ in range(N):
    X, Y, F = map(int, input().split())
    plants.append((X, Y, F))

result = frog_energy(N, K, plants)
print(result[0])
print(result[1])
for p in result[2]:
    print(plants[p-1][0], plants[p-1][1])
