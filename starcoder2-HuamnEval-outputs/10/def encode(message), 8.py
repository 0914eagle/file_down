
 def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            index = vowels.index(letter)
            if index == 4:
                encoded_message += vowels[0]
            else:
                encoded_message += vowels[index + 2]
        elif letter == ' ':
            encoded_message += ' '
        else:
            index = alphabet.index(letter)
            if index == 24:
                encoded_message += alphabet[0]
            elif index == 25:
                encoded_message += alphabet[1]
            else:
                encoded_message += alphabet[index + 2]
    return encoded_message
 