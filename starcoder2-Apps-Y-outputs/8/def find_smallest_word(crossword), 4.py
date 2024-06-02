
import sys

def find_smallest_word(crossword):
    smallest_word = None
    for i in range(len(crossword)):
        for j in range(len(crossword[0])):
            if crossword[i][j] != '#':
                # Check vertical
                if i + 1 < len(crossword) and crossword[i + 1][j] != '#':
                    word = crossword[i][j] + crossword[i + 1][j]
                    if smallest_word is None or word < smallest_word:
                        smallest_word = word
                # Check horizontal
                if j + 1 < len(crossword[0]) and crossword[i][j + 1] != '#':
                    word = crossword[i][j] + crossword[i][j + 1]
                    if smallest_word is None or word < smallest_word:
                        smallest_word = word
    return smallest_word

if __name__ == '__main__':
    rows, cols = map(int, sys.stdin.readline().split())
    crossword = []
    for _ in range(rows):
        crossword.append(sys.stdin.readline().strip())
    smallest_word = find_smallest_word(crossword)
    print(smallest_word)

