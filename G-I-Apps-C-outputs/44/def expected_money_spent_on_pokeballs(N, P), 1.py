
def expected_money_spent_on_pokeballs(N, P):
    if P == 0:
        return 5 * N
    
    q = 1 - P  # Probability of failing to catch a Pokemon with one Pokeball
    expected_spent = 0
    
    for k in range(N):
        expected_spent += (1 - q ** k) * q ** (N - 1) * 5
        
    return round(expected_spent, 9)

# Input
N, P = map(float, input().split())

# Output
print(expected_money_spent_on_pokeballs(int(N), P))
```
