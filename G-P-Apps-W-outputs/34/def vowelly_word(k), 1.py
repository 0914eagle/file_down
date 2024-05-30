
def vowelly_word(k):
    vowels = 'aeiou'
    
    if k < 5:
        return -1
    
    word = ''
    i = 0
    while i < k:
        word += vowels[i % 5]
        i += 1

    return word

# Input
k = 36

# Output
result = vowelly_word(k)
print(result)
```
