
def min_bitcoin_spend(HP_Y, ATK_Y, DEF_Y, HP_M, ATK_M, DEF_M, h, a, d):
    def check_win(HP_Y, ATK_Y, DEF_Y, HP_M, ATK_M, DEF_M):
        while HP_M > 0 and HP_Y > 0:
            HP_M -= max(0, ATK_Y - DEF_M)
            HP_Y -= max(0, ATK_M - DEF_Y)
        return HP_Y > 0

    min_bitcoins = float('inf')

    for hp in range(101):
        for atk in range(101):
            for deff in range(101):
                if check_win(HP_Y + hp, ATK_Y + atk, DEF_Y + deff, HP_M, ATK_M, DEF_M):
                    cost = hp*h + atk*a + deff*d
                    min_bitcoins = min(min_bitcoins, cost)

    return min_bitcoins

# Input
HP_Y, ATK_Y, DEF_Y = map(int, input().split())
HP_M, ATK_M, DEF_M = map(int, input().split())
h, a, d = map(int, input().split())

# Output
print(min_bitcoin_spend(HP_Y, ATK_Y, DEF_Y, HP_M, ATK_M, DEF_M, h, a, d))
```
