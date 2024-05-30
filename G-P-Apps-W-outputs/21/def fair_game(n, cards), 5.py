
def fair_game(n, cards):
    freq = {}
    for card in cards:
        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1
    
    if len(freq) != 2:
        print("NO")
    else:
        values = list(freq.values())
        if values[0] == values[1]:
            print("YES")
            print(*freq.keys())
        else:
            print("NO")

# Input parsing
n = int(input())
cards = [int(input()) for _ in range(n)]

# Call the function
fair_game(n, cards)
```
