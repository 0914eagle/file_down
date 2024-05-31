
import heapq

def find_path(N, K, plants):
    energy_levels = [0] * N
    jumps = [-1] * N
    visited = [False] * N

    min_heap = [(0, 0)]
    while min_heap:
        energy, plant = heapq.heappop(min_heap)
        if visited[plant]:
            continue
        visited[plant] = True
        energy_levels[plant] = energy

        for next_plant in range(N):
            if next_plant == plant or visited[next_plant]:
                continue
            x1, y1, _ = plants[plant]
            x2, y2, flies = plants[next_plant]
            cost = abs(x2 - x1) + abs(y2 - y1)
            if x2 > x1 or y2 > y1:
                cost *= K
            if energy_levels[plant] - cost >= 0:
                heapq.heappush(min_heap, (energy_levels[plant] - cost + flies, next_plant))
                jumps[next_plant] = plant

    path = [N]
    current = N
    while jumps[current] != -1:
        path.append(jumps[current] + 1)
        current = jumps[current]

    path.reverse()
    return energy_levels[N - 1], len(path), path

# Read input
N, K = map(int, input().split())
plants = [tuple(map(int, input().split())) for _ in range(N)]

# Find the optimal path
final_energy, num_plants, path = find_path(N, K, plants)

# Print output
print(final_energy)
print(num_plants)
for plant in path:
    print(f"{plants[plant-1][0]} {plants[plant-1][1]}")
