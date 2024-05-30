
def find_fair_game(cards):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    distinct_cards = list(set(cards))
    
    for card in distinct_cards:
        if card_count[card] != card_count[distinct_cards[0]]:
            print("NO")
            return
    
    print("YES")
    print(distinct_cards[0], distinct_cards[1])

# Input
n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

# Call the function with the cards
find_fair_game(cards)
```
