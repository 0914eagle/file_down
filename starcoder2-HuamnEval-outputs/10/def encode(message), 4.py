
def encode(message):
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            index = vowels.index(letter)
            encoded_message += alphabet[index + 2]
        elif letter in alphabet:
            index = alphabet.index(letter)
            encoded_message += alphabet[index].swapcase()
        else:
            encoded_message += letter
    return encoded_message
