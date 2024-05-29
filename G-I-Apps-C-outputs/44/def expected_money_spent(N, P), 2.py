
def expected_money_spent(N, P):
    def calc_expected(N, P, money):
        if N == 0:
            return money
        success = P * money
        failure = (1 - P) * (money + 5)  # Money spent on refill
        return P * success + (1 - P) * failure
    
    money = 5  # Initial money spent on Pokeballs
    expected = 0
    for i in range(N):
        expected += calc_expected(i, P, money)
    return round(expected, 9)

# Input
N, P = input().split()
N = int(N)
P = float(P)

# Output
print(expected_money_spent(N, P))
```
