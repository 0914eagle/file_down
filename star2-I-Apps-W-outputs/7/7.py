
def vowelly(k):
    vowels = 'aeiou'
    rows = 1
    while rows * rows < k:
        rows += 1
    cols = k // rows
    if rows * cols < k:
        rows += 1
        cols = k // rows
    grid = [[0] * cols for _ in range(rows)]
    for vowel in vowels:
        for i in range(rows):
            grid[i][i % cols] = vowel
    word = ''
    for i in range(rows):
        for j in range(cols):
            word += grid[i][j]
    return word

k = int(input())
word = vowelly(k)
if word:
    print(word)
else:
    print(-1)

