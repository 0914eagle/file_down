

def crossword(crossword):
    crossword = crossword.split('\n')
    crossword = [list(i) for i in crossword]
    words = []
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if crossword[i][j] != '#':
                if j < len(crossword[i]) - 1 and crossword[i][j + 1] != '#':
                    word = crossword[i][j]
                    k = j + 1
                    while k < len(crossword[i]) and crossword[i][k] != '#':
                        word += crossword[i][k]
                        k += 1
                    words.append(word)
                if i < len(crossword) - 1 and crossword[i + 1][j] != '#':
                    word = crossword[i][j]
                    k = i + 1
                    while k < len(crossword) and crossword[k][j] != '#':
                        word += crossword[k][j]
                        k += 1
                    words.append(word)
    return min(words)

if __name__ == '__main__':
    crossword = input()
    print(crossword(crossword))


