
def expected_spending(N, P):
    # Initialize the expected spending and the remaining Pokeballs
    expected_cost = 0
    remaining_pokeballs = 100

    # Loop through each encounter
    for _ in range(N):
        # Keep track of the current cost for this encounter
        cost = 0

        # Loop until either the Pokemon is caught or there are no more Pokeballs
        while True:
            cost += 1
            if remaining_pokeballs == 0:
                # Need to buy a new bag of Pokeballs
                cost += 5
                remaining_pokeballs = 100
            elif random.random() < P:
                # Pokemon is caught with probability P
                break
            remaining_pokeballs -= 1

        # Update the total expected spending
        expected_cost += cost

    # Return the average spending per encounter
    return expected_cost / N

# Example usage
N, P = 50, 0.125
result = expected_spending(N, P)
print(result)
```
