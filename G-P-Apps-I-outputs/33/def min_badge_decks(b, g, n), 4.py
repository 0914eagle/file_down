
def min_badge_decks(b, g, n):
    min_decks = min(n - b, n - g) + 1
    return min_decks

b = int(input())
g = int(input())
n = int(input())

result = min_badge_decks(b, g, n)
print(result)
```
