
def is_fair_game(n, cards):
    distinct_numbers = set(cards)
    
    if len(distinct_numbers) != 2:
        print("NO")
    elif cards.count(list(distinct_numbers)[0]) != n // 2:
        print("NO")
    else:
        print("YES")
        print(*distinct_numbers)

# Input parsing
n = int(input())
cards = [int(input()) for _ in range(n)]

is_fair_game(n, cards)
```
