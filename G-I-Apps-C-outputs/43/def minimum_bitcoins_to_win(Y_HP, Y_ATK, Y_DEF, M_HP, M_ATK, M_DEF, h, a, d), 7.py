
def minimum_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d):
    min_bitcoins = float('inf')
    for i in range(M_HP, Y_ATK + M_HP):
        for j in range(M_ATK, Y_DEF + M_ATK):
            for k in range(M_DEF, Y_DEF + M_DEF):
                if max(0, Y_ATK - k) >= M_HP:
                    min_bitcoins = min(min_bitcoins, (i - Y_HP) * h + (j - Y_ATK) * a + (k - Y_DEF) * d)
    return min_bitcoins

input_values = input().split()
Y_HP, Y_ATK, Y_DEF = map(int, input_values)

input_values = input().split()
M_HP, M_ATK, M_DEF = map(int, input_values)

input_values = input().split()
h, a, d = map(int, input_values)

result = minimum_bitcoins_to_win(Y_HP, Y_ATK, Y_DEF, M_HP, M_ATK, M_DEF, h, a, d)
print(result)
