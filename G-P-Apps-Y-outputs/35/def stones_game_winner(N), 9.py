
def stones_game_winner(N):
    if N % 2 == 0:
        return "Bob"
    else:
        return "Alice"

# Input
N = int(input("Enter the number of stones: "))
# Output
print(stones_game_winner(N))
```
