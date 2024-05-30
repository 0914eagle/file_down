
def stone_game_winner(N):
    if N % 2 == 1:
        return "Alice"
    else:
        return "Bob"

# Input
N = int(input())
# Output
print(stone_game_winner(N))
```
