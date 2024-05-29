
def min_bitcoins_to_win(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
    min_bitcoins = float('inf')
    
    for i in range(101):
        for j in range(101):
            for k in range(101):
                hp_needed = max(0, hp_m - (atk_y + i - def_m))
                hp_cost = max(0, hp_needed) * h
                atk_upgrade = max(0, atk_m - (atk_y + i))
                atk_cost = max(0, atk_upgrade) * a
                def_upgrade = max(0, def_m - (def_y + k))
                def_cost = max(0, def_upgrade) * d
                
                total_cost = hp_cost + atk_cost + def_cost
                if total_cost < min_bitcoins and (atk_y + i) > def_m and (atk_m) <= (def_y + k):
                    min_bitcoins = total_cost
    
    return min_bitcoins

# Input
hp_y, atk_y, def_y = map(int, input().split())
hp_m, atk_m, def_m = map(int, input().split())
h, a, d = map(int, input().split())

# Output
print(min_bitcoins_to_win(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d))
```
