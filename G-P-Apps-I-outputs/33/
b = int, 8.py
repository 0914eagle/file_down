
b = int(input())
g = int(input())
n = int(input())

min_decks = min(n, b, g, b+g-n) + 1
print(min_decks)
```
