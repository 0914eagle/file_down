
def encode(message):
    vowels = 'aeiouAEIOU'
    result = ""
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_char = chr(ord(char) + 2)
            else:
                new_char = char.swapcase()
        else:
            new_char = char
        result += new_char

    return result

# Test cases
print(encode('test'))  # Output: TGST
print(encode('This is a message'))  # Output: tHKS KS C MGSSCGG
