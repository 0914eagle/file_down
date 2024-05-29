
def encode(message):
    encoded_message = ""
    
    for char in message:
        if char.isalpha():
            if char.lower() in 'aeiou':
                index = (ord(char.lower()) - ord('a') + 2) % 26
                new_char = chr(ord('a') + index).upper()
            else:
                new_char = char.swapcase()
        else:
            new_char = char
        
        encoded_message += new_char

    return encoded_message

# Test cases
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'
