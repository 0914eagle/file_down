
def lexicographically_smallest_word(R, C, crossword):
    def find_horizontal_words(grid):
        words = set()
        for i in range(R):
            word = ""
            for j in range(C):
                if grid[i][j] != '#':
                    word += grid[i][j]
                else:
                    if len(word) >= 2:
                        words.add(word)
                    word = ""
            if len(word) >= 2:
                words.add(word)
        return words

    def find_vertical_words(grid):
        words = set()
        for j in range(C):
            word = ""
            for i in range(R):
                if grid[i][j] != '#':
                    word += grid[i][j]
                else:
                    if len(word) >= 2:
                        words.add(word)
                    word = ""
            if len(word) >= 2:
                words.add(word)
        return words

    horizontal_words = find_horizontal_words(crossword)
    vertical_words = find_vertical_words(crossword)

    smallest_word = min(horizontal_words.union(vertical_words))

    return smallest_word

# Input parsing
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

print(lexicographically_smallest_word(R, C, crossword))
```
