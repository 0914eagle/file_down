
def is_vowel(c):
    return c in ['a', 'e', 'i', 'o', 'u']

def vowelly_word(k):
    if k < 25:
        return -1
    
    rows = 5
    cols = k // rows
    if k % rows != 0:
        cols += 1
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelly_string = ''
    
    for i in range(rows):
        for j in range(cols):
            if i * cols + j < k:
                vowelly_string += vowels[(i+j) % 5]
    
    return vowelly_string

k = int(input())
result = vowelly_word(k)
print(result)
