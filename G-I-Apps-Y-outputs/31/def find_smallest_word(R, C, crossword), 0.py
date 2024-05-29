
def find_smallest_word(R, C, crossword):
    def horizontal_words():
        words = []
        for row in range(R):
            word = ""
            for col in range(C):
                if crossword[row][col] != "#":
                    word += crossword[row][col]
                else:
                    if len(word) >= 2:
                        words.append(word)
                    word = ""
            if len(word) >= 2:
                words.append(word)
        return words

    def vertical_words():
        words = []
        for col in range(C):
            word = ""
            for row in range(R):
                if crossword[row][col] != "#":
                    word += crossword[row][col]
                else:
                    if len(word) >= 2:
                        words.append(word)
                    word = ""
            if len(word) >= 2:
                words.append(word)
        return words

    words = horizontal_words()
    words.extend(vertical_words())

    return min(word for word in words if len(word) >= 2)

# Input Parsing
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

# Find and print the smallest word
print(find_smallest_word(R, C, crossword))
```
