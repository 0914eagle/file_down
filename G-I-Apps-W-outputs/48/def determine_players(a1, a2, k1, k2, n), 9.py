
def determine_players(a1, a2, k1, k2, n):
    min_players_out = max(0, n - (a1*(k1-1) + a2*(k2-1)))
    
    if k1 <= k2:
        max_players_out = min(a1, n//k1) + min(a2, (n - min(a1, n//k1)*k1) // k2)
    else:
        max_players_out = min(a2, n//k2) + min(a1, (n - min(a2, n//k2)*k2) // k1)
    
    print(min_players_out, max_players_out)

# Example inputs
a1 = 2
a2 = 3
k1 = 5
k2 = 1
n = 8
determine_players(a1, a2, k1, k2, n)

a1 = 3
a2 = 1
k1 = 6
k2 = 7
n = 25
determine_players(a1, a2, k1, k2, n)

a1 = 6
a2 = 4
k1 = 9
k2 = 10
n = 89
determine_players(a1, a2, k1, k2, n)
```
