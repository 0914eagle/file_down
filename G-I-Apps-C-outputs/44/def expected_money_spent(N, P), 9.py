
import sys

def expected_money_spent(N, P):
    # Initialize total money spent
    total_money = 0

    # Calculate the expected amount of money spent
    for i in range(1, N+1):
        money_spent = 5.0 * (1 - pow(1 - P, i))
        total_money += money_spent

    return total_money

# Read input values
input_data = sys.stdin.read().strip().split()
N = int(input_data[0])
P = float(input_data[1])

# Calculate and print the expected amount of money Zapray would spend on Pokeballs
print(f'{expected_money_spent(N, P):.9f}')
```
