
def calculate_players_out(a1, a2, k1, k2, n):
    min_players_out = max(0, n - (a1*(k1-1) + a2*(k2-1)))
    
    max_players_out = min(n, a1+k1-1, a2+k2-1)

    return min_players_out, max_players_out

# Input
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

# Calculate and output result
min_res, max_res = calculate_players_out(a1, a2, k1, k2, n)
print(min_res, max_res)
```
