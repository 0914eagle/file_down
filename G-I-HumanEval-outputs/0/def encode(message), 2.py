
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_char = chr(ord(char) + 2)
            else:
                if char.isupper():
                    encoded_char = char.lower()
                else:
                    encoded_char = char.upper()
        else:
            encoded_char = char
            
        encoded_message += encoded_char
    
    return encoded_message

# Test cases
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'
