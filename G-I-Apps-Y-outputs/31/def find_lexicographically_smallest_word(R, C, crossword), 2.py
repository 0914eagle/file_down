
def find_lexicographically_smallest_word(R, C, crossword):
    words = []
    
    # Check horizontal words
    for row in crossword:
        word = ''
        for char in row:
            if char != '#':
                word += char
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)
    
    # Check vertical words
    for j in range(C):
        word = ''
        for i in range(R):
            char = crossword[i][j]
            if char != '#':
                word += char
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)
    
    return min(word for word in words if len(word) >= 2)

# Input parsing
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

# Find and print the smallest word
print(find_lexicographically_smallest_word(R, C, crossword))
