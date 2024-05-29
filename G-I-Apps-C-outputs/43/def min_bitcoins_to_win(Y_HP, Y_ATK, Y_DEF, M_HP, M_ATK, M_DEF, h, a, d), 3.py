
def min_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d):
    min_bitcoins = float('inf')
    
    for i in range(max(0, M_ATK - Y_DEF), 1001):  # Check all possible attack points Master Yang can reach
        for j in range(max(0, M_DEF - Y_ATK), 1001):  # Check all possible defense points Master Yang can reach
            k = max(0, M_HP - (Y_ATK + i))  # Calculate the HP needed to beat the monster
            total_bitcoins = max(k * h, i * a, j * d)  # Calculate total bitcoins required
            
            if total_bitcoins < min_bitcoins:  # Update minimum bitcoins if needed
                min_bitcoins = total_bitcoins
    
    return min_bitcoins

# Input
Y_HP, Y_ATK, Y_DEF = map(int, input().split())
M_HP, M_ATK, M_DEF = map(int, input().split())
h, a, d = map(int, input().split())

# Output
print(min_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d))
```
