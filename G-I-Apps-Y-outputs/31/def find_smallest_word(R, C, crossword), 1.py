
def find_smallest_word(R, C, crossword):
    smallest_word = ""
    
    for i in range(R):
        word = ""
        for j in range(C):
            if crossword[i][j] != '#':
                word += crossword[i][j]
            else:
                if len(word) >= 2:
                    if smallest_word == "" or word < smallest_word:
                        smallest_word = word
                word = ""
        
        if len(word) >= 2:
            if smallest_word == "" or word < smallest_word:
                smallest_word = word
    
    for j in range(C):
        word = ""
        for i in range(R):
            if crossword[i][j] != '#':
                word += crossword[i][j]
            else:
                if len(word) >= 2:
                    if smallest_word == "" or word < smallest_word:
                        smallest_word = word
                word = ""
        
        if len(word) >= 2:
            if smallest_word == "" or word < smallest_word:
                smallest_word = word
    
    return smallest_word

# Input parsing
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

print(find_smallest_word(R, C, crossword))
```
