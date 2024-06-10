
def vowelly(k):
    vowels = 'aeiou'
    n = 1
    while n <= k:
        if k % n == 0:
            m = k // n
            grid = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    grid[i][j] = vowels[j % 5]
            for j in range(m):
                for i in range(n):
                    grid[i][j] = vowels[i % 5]
            word = ''
            for i in range(n):
                for j in range(m):
                    word += grid[i][j]
            return word
        n += 1
    return -1

k = int(input())
print(vowelly(k))

