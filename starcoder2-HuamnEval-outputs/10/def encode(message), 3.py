
def encode(message):
    vowels = 'aeiou'
    vowels_shifted = 'cghij'
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            encoded_message += vowels_shifted[vowels.index(letter)]
        elif letter.isupper():
            encoded_message += letter.lower()
        else:
            encoded_message += letter.upper()
    return encoded_message
 