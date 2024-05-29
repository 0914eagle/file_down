
def expected_money_to_spend_on_pokeballs(N, P):
    # Initialize variables
    money_spent = 0
    remaining_pokeballs = 100
    refill_cost = 5
    
    for _ in range(N):
        # Determine the number of pokeballs needed to catch the Pokemon
        pokeballs_needed = 1
        while True:
            if remaining_pokeballs == 0:
                money_spent += refill_cost
                remaining_pokeballs = 100
            remaining_pokeballs -= 1
            if remaining_pokeballs == 0:
                break
            if random.random() < P:  # Catch the Pokemon
                break
            pokeballs_needed += 1
        
        money_spent += pokeballs_needed / 100 * refill_cost
    
    return round(money_spent, 9)

# Input
N, P = map(float, input().split())

# Call the function and output the result
print(expected_money_to_spend_on_pokeballs(int(N), P))
```
