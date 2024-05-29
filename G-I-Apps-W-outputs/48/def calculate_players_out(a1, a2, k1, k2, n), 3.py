
def calculate_players_out(a1, a2, k1, k2, n):
    min_players_out = max(0, n - (a1 - 1) * k1 - (a2 - 1) * k2)
    
    max_players_out = 0
    while n > 0:
        if a1 * k1 <= n:
            max_players_out += a1
            n -= a1 * k1
            a1 = 0
        elif a2 * k2 <= n:
            max_players_out += a2
            n -= a2 * k2
            a2 = 0
        else:
            if n // k1 > a1:
                max_players_out += a1
                n -= a1 * k1
                a1 = 0
            else:
                max_players_out += n // k1
                n = 0

    return min_players_out, max_players_out

# Input
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

# Output
result = calculate_players_out(a1, a2, k1, k2, n)
print(result[0], result[1])
```
