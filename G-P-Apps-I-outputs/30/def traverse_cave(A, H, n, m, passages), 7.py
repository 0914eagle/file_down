
def traverse_cave(A, H, n, m, passages):
    max_health = H
    for i in range(n-1):
        enemy_attack = passages[i][2]
        enemy_health = passages[i][3]
        while H > 0 and enemy_health > 0:
            enemy_health -= A
            if enemy_health <= 0:
                break
            H -= enemy_attack
        if H <= 0:
            return 'Oh no'
        H = min(max_health, H + 1)  # Unnar restores 1 health point after defeating an enemy
    return H

# Input processing
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = []
for _ in range(m):
    e, b, a, h = map(int, input().split())
    passages.append((e, b, a, h))

result = traverse_cave(A, H, n, m, passages)
print(result)
```
