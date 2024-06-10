
def vowelly(k):
    vowels = "aeiou"
    rows = 1
    while rows * rows < k:
        rows += 1
    cols = k // rows
    if rows * cols != k:
        return -1
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    for vowel in vowels:
        for r in range(rows):
            for c in range(cols):
                grid[r][c] += vowel
    word = ""
    for r in range(rows):
        for c in range(cols):
            word += grid[r][c]
    return word

k = int(input())
print(vowelly(k))

