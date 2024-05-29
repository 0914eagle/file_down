
def encode(message):
    encoded_message = ''
    vowels = 'AEIOUaeiou'
    for char in message:
        if char.isalpha():
            if char.upper() in vowels:
                new_char = chr(ord(char)+2)
            else:
                if char.islower():
                    new_char = char.upper()
                else:
                    new_char = char.lower()
            encoded_message += new_char
        else:
            encoded_message += char
    return encoded_message

# Test cases
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'
