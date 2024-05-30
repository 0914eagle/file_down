
def vowelly_word(k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if k < 5:
        print("-1")
        return
    
    word = ''
    for i in range(k):
        word += vowels[i % 5]
    
    print(word)

# Example usage
k = 36
vowelly_word(k)
