
import heapq

def solve_cave_system(A, H, n, m, passages):
    graph = [[] for _ in range(n)]
    for e, b, a, h in passages:
        graph[e-1].append((b-1, a, h))

    min_health = [float('inf')] * n
    min_health[0] = H

    pq = []
    heapq.heappush(pq, (0, 0, H))
    while pq:
        cur_health, cur_area, cur_points = heapq.heappop(pq)
        if cur_area == n-1:
            return min_health[n-1]

        for next_area, enemy_attack, enemy_health in graph[cur_area]:
            next_health = cur_health

            while True:
                next_health -= enemy_attack
                if next_health <= 0:
                    break
                next_health += cur_points
                if next_health >= min_health[next_area]:
                    continue

                min_health[next_area] = next_health
                heapq.heappush(pq, (next_health, next_area, cur_points))

    return 'Oh no'

# Example inputs
A1, H1 = 1, 2
n1, m1 = 3, 2
passages1 = [(1, 2, 1, 2), (2, 3, 1, 2)]

A2, H2 = 1, 3
n2, m2 = 3, 2
passages2 = [(1, 2, 1, 2), (2, 3, 1, 2)]

print(solve_cave_system(A1, H1, n1, m1, passages1))  # Output: Oh no
print(solve_cave_system(A2, H2, n2, m2, passages2))  # Output: 1
```
