
def stone_game_winner(N):
    if N % 2 == 1:
        return "Alice"
    else:
        return "Bob"

# Sample Input
N = 1
print(stone_game_winner(N))  # Output: Alice

N = 2
print(stone_game_winner(N))  # Output: Bob
```
