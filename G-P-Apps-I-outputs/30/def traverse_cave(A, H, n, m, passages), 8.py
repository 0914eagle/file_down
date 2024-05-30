
def traverse_cave(A, H, n, m, passages):
    visited = [False] * (n + 1)
    health = H
    
    def dfs(area):
        nonlocal health
        visited[area] = True
        
        for p in passages[area]:
            next_area, enemy_attack, enemy_health = p
            
            if not visited[next_area]:
                enemy_rounds = (enemy_health + A - 1) // A
                player_rounds = (health + enemy_attack - 1) // enemy_attack
                
                if player_rounds >= enemy_rounds:
                    health = max(health - enemy_rounds * enemy_attack, 0)
                    dfs(next_area)
    
    dfs(1)
    
    if visited[n]:
        return health
    else:
        return 'Oh no'

# Input
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = {}
for _ in range(m):
    e, b, a, h = map(int, input().split())
    if e not in passages:
        passages[e] = []
    passages[e].append((b, a, h))

# Output
result = traverse_cave(A, H, n, m, passages)
print(result)
```
