
def find_smallest_word(crossword):
    rows, cols = len(crossword), len(crossword[0])
    words = []

    # Find horizontal words
    for row in range(rows):
        word = ''
        for col in range(cols):
            if crossword[row][col] != '#':
                word += crossword[row][col]
            elif len(word) >= 2:
                words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)

    # Find vertical words
    for col in range(cols):
        word = ''
        for row in range(rows):
            if crossword[row][col] != '#':
                word += crossword[row][col]
            elif len(word) >= 2:
                words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)

    return min(word for word in words if len(word) >= 2)

# Read input
R, C = map(int, input().split())
crossword = []
for _ in range(R):
    crossword.append(input())

print(find_smallest_word(crossword))
```
