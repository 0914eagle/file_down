
def crossword(grid):
    words = []
    for i in range(len(grid)):
        word = ""
        for j in range(len(grid[i])):
            if grid[i][j] != "#":
                word += grid[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)
    for j in range(len(grid[0])):
        word = ""
        for i in range(len(grid)):
            if grid[i][j] != "#":
                word += grid[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)
    return min(words)

grid = []
for _ in range(int(input())):
    grid.append(input())
print(crossword(grid))

