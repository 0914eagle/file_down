
def min_decks(b, g, n):
    min_decks = min(n, min(b, n) + min(g, n))
    return min_decks

# Input
b = int(input())
g = int(input())
n = int(input())

# Output
print(min_decks(b, g, n))
```
