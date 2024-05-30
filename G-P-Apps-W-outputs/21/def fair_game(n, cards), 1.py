
def fair_game(n, cards):
    count_dict = {}
    for card in cards:
        if card in count_dict:
            count_dict[card] += 1
        else:
            count_dict[card] = 1
    
    unique_cards = set(cards)
    
    if len(unique_cards) < 2:
        print("NO")
    else:
        for key, value in count_dict.items():
            if value == n // 2:
                print("YES")
                print(key, end=' ')
                for k in count_dict.keys():
                    if k != key:
                        print(k)
                break
        else:
            print("NO")

# Reading input
n = int(input())
cards = [int(input()) for _ in range(n)]

# Calling the function
fair_game(n, cards)
```
