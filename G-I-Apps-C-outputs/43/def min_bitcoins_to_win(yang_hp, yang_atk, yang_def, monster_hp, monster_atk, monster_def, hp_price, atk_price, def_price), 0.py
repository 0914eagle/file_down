
def min_bitcoins_to_win(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price):
    min_bitcoins = float('inf')

    for additional_hp in range(0, monster_atk + monster_def + 1):
        for additional_atk in range(0, max(1, monster_atk - yang_def)):
            for additional_def in range(0, max(1, monster_atk - yang_atk)):
                yang_final_hp = yang_hp + additional_hp
                yang_final_atk = yang_atk + additional_atk
                yang_final_def = yang_def + additional_def
                bitcoins = max(0, additional_hp * hp_price) + max(0, additional_atk * atk_price) + max(0, additional_def * def_price)

                if yang_final_hp > 0 and yang_final_hp > monster_hp:
                    min_bitcoins = min(min_bitcoins, bitcoins)

    return min_bitcoins

# Input parsing
yang_hp, yang_atk, yang_def = map(int, input().split())
monster_hp, monster_atk, monster_def = map(int, input().split())
hp_price, atk_price, def_price = map(int, input().split())

result = min_bitcoins_to_win(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price)
print(result)
