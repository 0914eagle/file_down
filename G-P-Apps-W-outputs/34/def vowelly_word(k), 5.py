
def vowelly_word(k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if k < 25:
        return -1
    
    rows = 5
    cols = k // rows
    
    if k % rows != 0:
        cols += 1
    
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    idx = 0
    for i in range(rows):
        for j in range(cols):
            if idx < k:
                grid[i][j] = vowels[idx % 5]
                idx += 1
    
    vowelly_word = ''
    for j in range(cols):
        for i in range(rows):
            vowelly_word += grid[i][j]
    
    return vowelly_word

k = int(input())
result = vowelly_word(k)
print(result)
```
```plaintext
