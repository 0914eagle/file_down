
 def encode(message):
    message = message.lower()
    vowels = 'aeiou'
    new_message = ''
    for char in message:
        if char in vowels:
            new_message += vowels[vowels.index(char) + 2]
        elif char == 'y':
            new_message += 'a'
        elif char == 'z':
            new_message += 'b'
        else:
            new_message += chr(ord(char) + 1)
    return new_message.upper()
 