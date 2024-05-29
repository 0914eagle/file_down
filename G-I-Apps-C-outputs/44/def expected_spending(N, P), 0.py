
def expected_spending(N, P):
    prob_fail = 1 - P
    prob_success = P

    expected_money = 5  # Initial cost of 100 Pokeballs

    for _ in range(N):
        expected_money += prob_success * (0) + prob_fail * expected_money

    return round(expected_money, 9)

# Read input
N, P = map(float, input().split())

# Call the function and print the result
print(expected_spending(int(N), P))
```
