
def stone_game_winner(N):
    # If the number of stones is odd, Alice wins, else Bob wins
    if N % 2 == 1:
        return "Alice"
    else:
        return "Bob"

# Reading input
N = int(input())

# Getting the winner
winner = stone_game_winner(N)
print(winner)
```
