
def find_smallest_word(crossword):
    smallest_word = ""
    for row in crossword:
        for i in range(len(row)):
            if row[i] == "#":
                continue
            word = ""
            for j in range(i, len(row)):
                if row[j] == "#":
                    break
                word += row[j]
            if len(word) < 2:
                continue
            if smallest_word == "" or word < smallest_word:
                smallest_word = word
    for i in range(len(crossword[0])):
        word = ""
        for j in range(len(crossword)):
            if crossword[j][i] == "#":
                break
            word += crossword[j][i]
        if len(word) < 2:
            continue
        if smallest_word == "" or word < smallest_word:
            smallest_word = word
    return smallest_word

R, C = map(int, input().split())
crossword = []
for _ in range(R):
    crossword.append(input())
print(find_smallest_word(crossword))

