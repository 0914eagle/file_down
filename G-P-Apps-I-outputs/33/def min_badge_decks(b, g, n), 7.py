
def min_badge_decks(b, g, n):
    min_decks = min(b, n) + min(g, n)
    return min_decks - n + 1

# Read input
b = int(input())
g = int(input())
n = int(input())
# Call the function and output the result
print(min_badge_decks(b, g, n))
```
