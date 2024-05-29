
def expected_money_spent(N, P):
    prob_fail = 1 - P
    expected_cost = 0

    for i in range(1, N+1):
        expected_cost += (5 + expected_cost * prob_fail) * P

    return round(expected_cost, 9)

# Input
N, P = map(float, input().split())

# Output
print(expected_money_spent(int(N), P))
```
