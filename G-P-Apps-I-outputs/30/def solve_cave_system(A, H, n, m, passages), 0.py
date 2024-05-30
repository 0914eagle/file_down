
def solve_cave_system(A, H, n, m, passages):
    dp = [0] * (n + 1)
    dp[1] = H
    
    for _ in range(n + 1):
        updated = False
        for e, b, a, h in passages:
            if dp[e] <= 0:
                continue
                
            damage_to_enemy = (h + A - 1) // A
            damage_to_unnar = (dp[e] + a - 1) // a
            
            if damage_to_enemy < damage_to_unnar and dp[b] < dp[e] - damage_to_enemy * a:
                dp[b] = dp[e] - damage_to_enemy * a
                updated = True
        
        if not updated:
            break
    
    if dp[n] <= 0:
        return "Oh no"
    else:
        return dp[n]

# Input parsing
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = [list(map(int, input().split())) for _ in range(m)]

result = solve_cave_system(A, H, n, m, passages)
print(result)
```
