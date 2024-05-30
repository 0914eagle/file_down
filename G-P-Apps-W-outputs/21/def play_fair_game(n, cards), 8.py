
def play_fair_game(n, cards):
    counts = {}
    for card in cards:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1

    distinct_cards = list(set(cards))

    for card in distinct_cards:
        if counts[card] != n // 2:
            for other_card in distinct_cards:
                if counts[other_card] == n // 2:
                    print("YES")
                    print(card, other_card)
                    return

    print("NO")

# Input processing
n = int(input())
cards = [int(input()) for _ in range(n)]

# Call the function
play_fair_game(n, cards)
```
