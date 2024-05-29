
def find_smallest_word(R, C, crossword):
    words = []
    
    # Check horizontally
    for i in range(R):
        word = ""
        for j in range(C):
            if crossword[i][j] != "#":
                word += crossword[i][j]
            elif crossword[i][j] == "#" and len(word) >= 2:
                words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)
    
    # Check vertically
    for j in range(C):
        word = ""
        for i in range(R):
            if crossword[i][j] != "#":
                word += crossword[i][j]
            elif crossword[i][j] == "#" and len(word) >= 2:
                words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)
    
    return min(words)

# Input parsing
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

# Find and output the lexicographically smallest word
print(find_smallest_word(R, C, crossword))
```
