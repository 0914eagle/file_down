
def translate_new_alphabet(text):
    translation = {
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
        't': '\'][][',
        'u': '|_|',
        'v': '\/',
        'w': '\/\/',
        'x': '}{',
        'y': '`/',
        'z': '2',
        'A': '@',
        'B': '8',
        'C': '(',
        'D': '|)',
        'E': '3',
        'F': '#',
        'G': '6',
        'H': '[-]',
        'I': '|',
        'J': '_|',
        'K': '|<',
        'L': '1',
        'M': '[]\/[]',
        'N': '[]\[]',
        'O': '0',
        'P': '|D',
        'Q': '(,)',
        'R': '|Z',
        'S': '$',
        'T': '\'][][',
        'U': '|_|',
        'V': '\/',
        'W': '\/\/',
        'X': '}{',
        'Y': '`/',
        'Z': '2'
    }

    new_text = ''
    for char in text:
        if char in translation:
            new_text += translation[char]
        else:
            new_text += char

    return new_text

# Test the function with sample inputs
print(translate_new_alphabet("All your base are belong to us."))
print(translate_new_alphabet("What's the Frequency, Kenneth?"))
```
