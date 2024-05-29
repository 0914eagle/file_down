
def calculate_players_out(a1, a2, k1, k2, n):
    min_players_out = max(0, n - (a1*(k1-1) + a2*(k2-1)))
    
    max_players_out = min(n, a1 + a2 - (a1*(k1-1) + a2*(k2-1)))
    
    print(min_players_out, max_players_out)

# Input
a1 = 2
a2 = 3
k1 = 5
k2 = 1
n = 8

# Output
calculate_players_out(a1, a2, k1, k2, n)
```
