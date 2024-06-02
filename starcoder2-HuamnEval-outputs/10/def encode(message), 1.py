
def encode(message):
    vowels = 'aeiou'
    vowels_shifted = 'cghij'
    message = message.lower()
    encoded_message = ''
    for char in message:
        if char in vowels:
            index = vowels.index(char)
            encoded_message += vowels_shifted[index]
        else:
            encoded_message += char.swapcase()
    return encoded_message
