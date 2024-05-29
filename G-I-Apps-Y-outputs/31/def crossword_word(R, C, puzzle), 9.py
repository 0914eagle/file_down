
def crossword_word(R, C, puzzle):
    words = set()
    
    # Find all horizontal words
    for row in puzzle:
        word = ""
        for char in row:
            if char == "#":
                if len(word) >= 2:
                    words.add(word)
                word = ""
            else:
                word += char
        if len(word) >= 2:
            words.add(word)
    
    # Find all vertical words
    for j in range(C):
        word = ""
        for i in range(R):
            if puzzle[i][j] == "#":
                if len(word) >= 2:
                    words.add(word)
                word = ""
            else:
                word += puzzle[i][j]
        if len(word) >= 2:
            words.add(word)
    
    return min(words)

# Input parsing and function call
R, C = map(int, input().split())
puzzle = [input() for _ in range(R)]

print(crossword_word(R, C, puzzle))
