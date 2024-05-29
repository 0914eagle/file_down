
def find_smallest_word(R, C, crossword):
    def is_valid_word(word):
        return len(word) >= 2
    
    def check_word(word):
        if is_valid_word(word):
            if smallest_word[0] == '' or word < smallest_word[0]:
                smallest_word[0] = word

    smallest_word = ['']
    
    # Check horizontally
    for i in range(R):
        word = ''
        for j in range(C):
            if crossword[i][j] != '#':
                word += crossword[i][j]
            else:
                check_word(word)
                word = ''
        check_word(word)
    
    # Check vertically
    for j in range(C):
        word = ''
        for i in range(R):
            if crossword[i][j] != '#':
                word += crossword[i][j]
            else:
                check_word(word)
                word = ''
        check_word(word)
    
    return smallest_word[0]

# Input
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

# Output
print(find_smallest_word(R, C, crossword))
```
