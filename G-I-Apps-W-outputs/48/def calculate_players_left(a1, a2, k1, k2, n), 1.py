
def calculate_players_left(a1, a2, k1, k2, n):
    min_players_left = max(0, n - (a1 - 1) * k1 - (a2 - 1) * k2)
    
    max_players_left = 0
    remaining_cards = n
    max_players_left += min(a1, remaining_cards // k1)
    remaining_cards -= min(a1, remaining_cards // k1) * k1
    max_players_left += min(a2, remaining_cards // k2)
    
    return min_players_left, max_players_left

# Input
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

# Output
min_players, max_players = calculate_players_left(a1, a2, k1, k2, n)
print(min_players, max_players)
```
