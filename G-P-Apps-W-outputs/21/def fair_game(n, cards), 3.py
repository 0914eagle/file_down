
def fair_game(n, cards):
    occurrences = {}
    
    # Count occurrences of each number
    for card in cards:
        if card not in occurrences:
            occurrences[card] = 0
        occurrences[card] += 1
    
    # Check if there are only two distinct numbers
    if len(occurrences) != 2:
        print("NO")
        return
    
    # Check if the counts of the two numbers are equal
    if occurrences[cards[0]] != occurrences[cards[1]]:
        print("NO")
        return
    
    print("YES")
    print(cards[0], cards[1])

# Read input
n = int(input())
cards = [int(input()) for _ in range(n)]

# Call the function
fair_game(n, cards)
```
