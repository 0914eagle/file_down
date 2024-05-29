
def expected_spending(N, P):
    cost = 0
    prob_fail = 1 - P
    for i in range(1, N+1):
        prob_no_catch = (prob_fail) ** 100
        cost += 5 * prob_no_catch * (1 - prob_no_catch) ** (i - 1) * P * 100
    return round(cost, 9)

N, P = map(float, input().split())
print(expected_spending(int(N), P))
```
