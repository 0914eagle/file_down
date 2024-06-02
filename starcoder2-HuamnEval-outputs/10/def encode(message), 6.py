
def encode(message):
    vowels = 'aeiou'
    new_message = ''
    for letter in message:
        if letter.lower() in vowels:
            new_letter = chr(ord(letter) + 2)
            if new_letter in vowels:
                new_letter = chr(ord(new_letter) - 2)
            new_message += new_letter
        else:
            new_message += letter
    return new_message
