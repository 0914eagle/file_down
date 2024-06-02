
def crossword(r,c):
    cross = []
    for i in range(r):
        cross.append(input())
    words = []
    for i in range(r):
        word = ""
        for j in range(c):
            if cross[i][j] != "#":
                word += cross[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)
    for i in range(c):
        word = ""
        for j in range(r):
            if cross[j][i] != "#":
                word += cross[j][i]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)
    words.sort()
    return words[0]

r,c = map(int, input().split())
print(crossword(r,c))

