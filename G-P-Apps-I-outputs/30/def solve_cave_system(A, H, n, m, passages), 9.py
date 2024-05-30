
def solve_cave_system(A, H, n, m, passages):
    def traverse_area(area, health):
        if area == n:
            return health
        if health <= 0:
            return -1
        max_health = -1
        for passage in passages:
            if passage[0] == area:
                enemy_health = passage[3]
                enemy_attack = passage[2]
                new_health = max(0, health - enemy_attack)
                enemy_new_health = max(0, enemy_health - A)
                rec_health = traverse_area(passage[1], new_health)
                if rec_health != -1:
                    max_health = max(max_health, rec_health + H - new_health)
        return max_health

    result = traverse_area(1, H)
    if result == -1:
        print('Oh no')
    else:
        print(result)

# Input parsing
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = [list(map(int, input().split())) for _ in range(m)]

solve_cave_system(A, H, n, m, passages)
```
