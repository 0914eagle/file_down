
def stones_game_winner(N):
    if N % 2 == 1:
        return "Alice"
    else:
        return "Bob"

# Input
N = int(input())
print(stones_game_winner(N))
```
