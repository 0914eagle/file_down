
def vowelly(k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for n in range(1, k+1):
        if k % n == 0:
            m = k // n
            grid = [[None for _ in range(m)] for _ in range(n)]
            for vowel in vowels:
                for i in range(n):
                    for j in range(m):
                        if grid[i][j] is None:
                            grid[i][j] = vowel
                            break
                    if all(grid[i][j] is not None for j in range(m)):
                        break
                if all(grid[i][j] is not None for i in range(n) for j in range(m)):
                    break
            if all(grid[i][j] is not None for i in range(n) for j in range(m)):
                return ''.join(grid[i][j] for i in range(n) for j in range(m))
    return -1

