
def find_lexicographically_smallest_word(R, C, crossword):
    smallest_word = None

    for r in range(R):
        for c in range(C):
            if crossword[r][c] != '#':
                # Find horizontal word
                word_h = ""
                c_h = c
                while c_h < C and crossword[r][c_h] != '#':
                    word_h += crossword[r][c_h]
                    c_h += 1

                if len(word_h) >= 2 and (smallest_word is None or word_h < smallest_word):
                    smallest_word = word_h

                # Find vertical word
                word_v = ""
                r_v = r
                while r_v < R and crossword[r_v][c] != '#':
                    word_v += crossword[r_v][c]
                    r_v += 1

                if len(word_v) >= 2 and (smallest_word is None or word_v < smallest_word):
                    smallest_word = word_v

    return smallest_word

# Read input
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

# Find and output the lexicographically smallest word
print(find_lexicographically_smallest_word(R, C, crossword))
```
