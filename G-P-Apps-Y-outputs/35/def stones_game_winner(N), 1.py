
def stones_game_winner(N):
    if N % 2 == 1:
        return "Alice"
    else:
        return "Bob"

# Read input
N = int(input())
# Output the winner
print(stones_game_winner(N))
```
