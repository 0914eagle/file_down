
def min_decks(b, g, n):
    min_decks = float('inf')
    for i in range(n + 1):
        if i <= b and n - i <= g:
            min_decks = min(min_decks, n)
    return min_decks

b = int(input())
g = int(input())
n = int(input())
print(min_decks(b, g, n))
```
