
def find_smallest_word(R, C, puzzle):
    words = set()
    for i in range(R):
        word = ''
        for j in range(C):
            if puzzle[i][j] != '#':
                word += puzzle[i][j]
            else:
                if len(word) >= 2:
                    words.add(word)
                word = ''
        if len(word) >= 2:
            words.add(word)
    
    for j in range(C):
        word = ''
        for i in range(R):
            if puzzle[i][j] != '#':
                word += puzzle[i][j]
            else:
                if len(word) >= 2:
                    words.add(word)
                word = ''
        if len(word) >= 2:
            words.add(word)
    
    return min(words)

# Sample input
R, C = 4, 4
puzzle = [
    "luka",
    "o#a#",
    "kula",
    "i#a#"
]

print(find_smallest_word(R, C, puzzle))
```
