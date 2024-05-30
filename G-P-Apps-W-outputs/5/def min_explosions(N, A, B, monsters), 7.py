
def min_explosions(N, A, B, monsters):
    remaining_monsters = []
    total_explosions = 0
    
    for monster in monsters:
        if monster <= A:
            remaining_monsters.append(0)
        else:
            remaining_monsters.append(monster - A)
    
    while sum(remaining_monsters) > 0:
        max_health = max(remaining_monsters)
        total_explosions += 1
        for i in range(N):
            if remaining_monsters[i] == max_health:
                remaining_monsters[i] = max(0, remaining_monsters[i] - A)
            else:
                remaining_monsters[i] = max(0, remaining_monsters[i] - B)
    
    return total_explosions

# Reading input
N, A, B = map(int, input().split())
monsters = [int(input()) for _ in range(N)]

# Output the minimum number of explosions needed
print(min_explosions(N, A, B, monsters))
```
