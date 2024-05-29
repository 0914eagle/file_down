
def possible_players(a1, a2, k1, k2, n):
    min_players = max(0, n - (a1 - 1) * k1 - (a2 - 1) * k2)
    
    remaining_cards = n
    max_players = 0
    for i in range(min(a1, remaining_cards // k1) + 1):
        remaining_cards_a2 = max(0, remaining_cards - i * k1)
        j = min(a2, remaining_cards_a2 // k2)
        max_players = max(max_players, i + j)
        
    return min_players, max_players

# Read input
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

# Call the function and print the output
min_players, max_players = possible_players(a1, a2, k1, k2, n)
print(min_players, max_players)
```
