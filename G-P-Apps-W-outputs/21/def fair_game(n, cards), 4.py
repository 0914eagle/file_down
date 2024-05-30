
def fair_game(n, cards):
    counts = {}
    for card in cards:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    if len(counts) != 2:
        print("NO")
    else:
        vals = list(counts.values())
        if vals[0] == vals[1]:
            print("YES")
            print(*counts.keys())
        else:
            print("NO")

# Input parsing
n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

fair_game(n, cards)
```
