
def can_traverse_cave(A, H, n, m, passages):
    max_health = H
    for _ in range(n-1):
        enemy_attack, enemy_health = passages[_]
        while enemy_health > 0 and H > 0:
            H -= enemy_attack
            enemy_health -= A
        if H <= 0:
            return "Oh no"
        max_health = max(max_health, H)
    return max_health

# Input parsing
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = [list(map(int, input().split())) for _ in range(m)]

result = can_traverse_cave(A, H, n, m, passages)
print(result)
```
