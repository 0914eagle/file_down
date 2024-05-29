
def minimum_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d):
    min_bitcoins = float('inf')

    for i in range(0, max(M_ATK + M_DEF - Y_ATK, 0) + 1):
        for j in range(0, max(Y_ATK + Y_DEF - M_ATK, 0) + 1):
            HP_needed = max(M_HP - ((Y_ATK + i) - M_DEF), 0)
            ATK_needed = max(M_ATK - ((Y_DEF + j) - M_ATK), 0)
            bitcoins = i * a + j * d + HP_needed * h
            min_bitcoins = min(min_bitcoins, bitcoins)

    return min_bitcoins

# Input
input_data = list(map(int, input().split()))
Y_HP, Y_ATK, Y_DEF = input_data[:3]
M_HP, M_ATK, M_DEF = input_data[3:6]
h, a, d = input_data[6:]

# Output
print(minimum_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d))
