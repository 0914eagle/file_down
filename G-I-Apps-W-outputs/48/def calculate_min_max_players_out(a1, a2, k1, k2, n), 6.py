
def calculate_min_max_players_out(a1, a2, k1, k2, n):
    total_cards_possible = a1 * k1 + a2 * k2
    remaining_cards = n
    min_players_out = max(0, n - min(k1, k2))
    
    if n <= total_cards_possible:
        max_players_out = min(a1, n // k1) + min(a2, n // k2)
    else:
        remaining_cards -= min(a1, n // k1) * k1
        remaining_cards -= min(a2, n // k2) * k2
        max_players_out = a1 + a2 - min(a1, remaining_cards // k2) - min(a2, remaining_cards // k1)
    
    print(min_players_out, max_players_out)

a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

calculate_min_max_players_out(a1, a2, k1, k2, n)
```
