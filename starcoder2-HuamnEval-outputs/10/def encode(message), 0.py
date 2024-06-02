
 def encode(message):
    vowels = 'aeiou'
    new_message = ''
    for letter in message:
        if letter in vowels:
            new_message += chr(ord(letter) + 2)
        elif letter.isupper():
            new_message += letter.lower()
        else:
            new_message += letter.upper()
    return new_message
 