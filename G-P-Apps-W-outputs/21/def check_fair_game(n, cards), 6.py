
def check_fair_game(n, cards):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    if len(card_count) != 2:
        print("NO")
    else:
        for card, count in card_count.items():
            if count != n//2:
                print("NO")
                return
            else:
                print("YES")
                print(*card_count.keys())
                return

# Example Input
n = 4
cards = [11, 27, 27, 11]
check_fair_game(n, cards)

n = 2
cards = [6, 6]
check_fair_game(n, cards)

n = 6
cards = [10, 20, 30, 20, 10, 20]
check_fair_game(n, cards)

n = 6
cards = [1, 1, 2, 2, 3, 3]
check_fair_game(n, cards)
```
