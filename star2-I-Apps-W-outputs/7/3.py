
def vowelly(k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    rows = 1
    while rows <= k:
        cols = k // rows
        if rows * cols == k:
            grid = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    grid[i][j] = vowels[(i + j) % len(vowels)]
            word = ""
            for i in range(rows):
                for j in range(cols):
                    word += grid[i][j]
            return word
        rows += 1
    return -1

k = int(input())
print(vowelly(k))

