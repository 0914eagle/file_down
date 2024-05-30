
def translate_to_new_alphabet(text):
    translation_table = {
        'a': '@',
        'b': '8',
        'c': '(',
        'd': '|)',
        'e': '3',
        'f': '#',
        'g': '6',
        'h': '[-]',
        'i': '|',
        'j': '_|',
        'k': '|<',
        'l': '1',
        'm': '[]\/[]',
        'n': '[]\[]',
        'o': '0',
        'p': '|D',
        'q': '(,)',
        'r': '|Z',
        's': '$',
        't': '\'][\'',
        'u': '|_|',
        'v': '\/\\/',
        'w': '\/\/',
        'x': '}{',
        'y': '`/',
        'z': '2'
    }
    
    new_text = ''
    for char in text:
        if char.lower() in translation_table:
            if char.isupper():
                new_text += translation_table[char.lower()].upper()
            else:
                new_text += translation_table[char]
        else:
            new_text += char
    
    return new_text

# Test the function with sample inputs
print(translate_to_new_alphabet("All your base are belong to us."))
print(translate_to_new_alphabet("What's the Frequency, Kenneth?"))
```
