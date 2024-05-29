
def calculate_players_out(a1, a2, k1, k2, n):
    min_players_out = max(0, n - (a1 - 1) * k1 - (a2 - 1) * k2)
    
    total_possible_yellow_cards = a1 * k1 + a2 * k2
    max_players_out = min(a1, n // k1) + min(a2, (n - min(a1, n // k1) * k1) // k2)
    
    return min_players_out, max_players_out

# Input
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

# Output
min_players_out, max_players_out = calculate_players_out(a1, a2, k1, k2, n)
print(min_players_out, max_players_out)
```
