
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = (ord(char) + 2 - ord('a')) % 26
                new_char = chr(ord('a') + index) if char.islower() else chr(ord('A') + index)
            else:
                new_char = char.swapcase()
            encoded_message += new_char
        else:
            encoded_message += char
    
    return encoded_message

# Test cases
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'
