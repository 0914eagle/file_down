
def min_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d):
    min_bitcoins = float('inf')

    for i in range(M_ATK + 1, Y_ATK + 100):
        for j in range(M_DEF + 1, Y_DEF + 100):
            for k in range((M_HP + i - 1) // i, (Y_HP + M_ATK - 1) // M_ATK + 100):
                bitcoins = max(0, (k * i - Y_HP) * h) + max(0, (k * j - Y_DEF) * d) + max(0, (k * M_ATK - Y_DEF) * a)
                min_bitcoins = min(min_bitcoins, bitcoins)

    return min_bitcoins

# Input
inputs = input().split()
Y_HP, Y_ATK, Y_DEF = map(int, inputs)

inputs = input().split()
M_HP, M_ATK, M_DEF = map(int, inputs)

inputs = input().split()
h, a, d = map(int, inputs)

# Output
result = min_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d)
print(result)
