
def min_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d):
    min_bitcoins = float('inf')

    for i in range(M_ATK + 1):  
        for j in range(M_DEF + 1):
            additional_HP = max(0, M_ATK - (Y_DEF + j))
            additional_ATK = max(0, Y_ATK - (M_DEF + i))
            total_bitcoins = max(0, additional_HP) * h + max(0, additional_ATK) * a + j * d
            min_bitcoins = min(min_bitcoins, total_bitcoins)

    return min_bitcoins

# Input parsing
Y_HP, Y_ATK, Y_DEF = map(int, input().split())
M_HP, M_ATK, M_DEF = map(int, input().split())
h, a, d = map(int, input().split())

# Calculate and print the result
print(min_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d))
```
