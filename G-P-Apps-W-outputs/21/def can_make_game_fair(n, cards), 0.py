
def can_make_game_fair(n, cards):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    if len(card_count) != 2:
        print("NO")
    else:
        cards_list = list(card_count.keys())
        if card_count[cards_list[0]] == card_count[cards_list[1]]:
            print("YES")
            print(cards_list[0], cards_list[1])
        else:
            print("NO")

# Input processing
n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

# Check if the game can be fair
can_make_game_fair(n, cards)
```
