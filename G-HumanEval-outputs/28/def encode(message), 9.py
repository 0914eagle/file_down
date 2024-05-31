
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += chr(ord(char) + 2).swapcase()
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message

# Test cases
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'
