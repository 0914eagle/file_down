
def can_traverse_cave(A, H, n, m, passages):
    visited = [False] * n
    health = H
    stack = [0]

    while stack:
        current_area = stack.pop()
        visited[current_area] = True

        for i in range(m):
            if passages[i][0] == current_area:
                enemy_a = passages[i][2]
                enemy_h = passages[i][3]

                while enemy_h > 0 and health > 0:
                    enemy_h -= A
                    if enemy_h <= 0:
                        break
                    health -= enemy_a

                if health <= 0:
                    return "Oh no"

                next_area = passages[i][1]
                if not visited[next_area]:
                    stack.append(next_area)

    return health

# Example usage
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = [list(map(int, input().split())) for _ in range(m)]

result = can_traverse_cave(A, H, n, m, passages)
print(result)
```
