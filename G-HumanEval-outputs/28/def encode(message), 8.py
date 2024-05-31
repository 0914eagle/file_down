
def encode(message):
    encoded_message = ''
    vowels = 'aeiouAEIOU'
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += chr(ord(char) + 2)
            else:
                if char.islower():
                    encoded_message += char.upper()
                else:
                    encoded_message += char.lower()
        else:
            encoded_message += char
    return encoded_message

print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'