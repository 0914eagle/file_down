
def vowelly_word(k):
    vowels = 'aeiou'
    
    if k < 25:
        return -1
    
    word = ''
    for i in range(5):
        for j in range(5):
            word += vowels[(i+j)%5]
    
    remaining_chars = k - 25
    for i in range(remaining_chars):
        word += vowels[i%5]
    
    return word

# Example usage
k = 36
result = vowelly_word(k)
print(result)
