
b = int(input())
g = int(input())
n = int(input())

min_decks = min(n, min(b, g) + 1)
print(min_decks)
