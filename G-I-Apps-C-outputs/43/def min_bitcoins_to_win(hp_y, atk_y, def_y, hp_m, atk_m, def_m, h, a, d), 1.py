
def min_bitcoins_to_win(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
    min_bitcoins = float('inf')

    for i in range(101):
        for j in range(101):
            for k in range(101):
                if atk_m - (def_y + j) <= 0:
                    continue
                turns_needed = (hp_m + atk_m - 1) // (atk_y - (def_m + k))
                hp_needed = max(turns_needed * (atk_m - (def_y + j)), hp_m)
                bitcoins_required = i * h + j * a + k * d

                if hp_y > hp_needed and bitcoins_required < min_bitcoins:
                    min_bitcoins = bitcoins_required

    return min_bitcoins

# Input
hp_y, atk_y, def_y = map(int, input().split())
hp_m, atk_m, def_m = map(int, input().split())
h, a, d = map(int, input().split())

# Output
print(min_bitcoins_to_win(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d))
```
