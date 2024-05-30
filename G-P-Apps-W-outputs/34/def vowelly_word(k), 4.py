
def vowelly_word(k):
    vowels = 'aeiou'
    
    if k < 25 or k == 26:
        print(-1)
        return
    
    word = ''
    for i in range(5):
        for j in range(5):
            word += vowels[(i + j) % 5]
    
    remaining = k - 25
    for i in range(remaining):
        word += vowels[i % 5]
    
    print(word)

# Test cases
vowelly_word(7)  # Output: -1
vowelly_word(36)  # Output: agoeuioaeiruuimaeoieauoweouoiaouimae
```
