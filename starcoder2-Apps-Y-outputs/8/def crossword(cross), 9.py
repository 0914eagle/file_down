
def crossword(cross):
    cross = cross.split("\n")
    cross = [list(i) for i in cross]
    cross = [[i for i in j if i != "#"] for j in cross]
    cross = ["".join(i) for i in cross]
    cross = sorted(cross)
    return cross[0]

print(crossword(input()))

