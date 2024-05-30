
def solve_game(n, cards):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    for key, value in card_count.items():
        if value != n // 2:
            continue
        for k, v in card_count.items():
            if k != key and v == n // 2:
                return "YES\n{} {}".format(key, k)
    
    return "NO"

# Input processing
n = int(input())
cards = [int(input()) for _ in range(n)]

# Solve the game and print the result
print(solve_game(n, cards))
```
