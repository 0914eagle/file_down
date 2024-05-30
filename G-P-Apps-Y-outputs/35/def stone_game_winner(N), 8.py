
def stone_game_winner(N):
    if N % 2 == 0:
        return "Bob"
    else:
        return "Alice"

# Read input
N = int(input())

# Determine the winner
winner = stone_game_winner(N)

# Output the winner
print(winner)
```
