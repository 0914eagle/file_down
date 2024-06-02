
def encode(message):
    vowels = 'aeiou'
    new_message = ''
    for letter in message:
        if letter in vowels:
            new_message += vowels[vowels.index(letter) + 2]
        else:
            new_message += letter.swapcase()
    return new_message
 