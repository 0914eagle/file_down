
def new_alphabet_translation(text):
    translation_dict = {
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
        't': '']['',
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
        'T': '']['',
        'U': '|_|',
        'V': '\/',
        'W': '\/\/',
        'X': '}{',
        'Y': '`/',
        'Z': '2'
    }
    
    translated_text = ''
    
    for char in text:
        if char in translation_dict:
            translated_text += translation_dict[char]
        else:
            translated_text += char
    
    return translated_text

# Test the function
print(new_alphabet_translation("Hello World!"))  # Output: [-]3110 \/\/0|Z1|)!
print(new_alphabet_translation("All your base are belong to us."))  # Output: @11 `/0|_||Z [email protected]$3 @|Z3 8310[]\[]6 ']['0 |_|$.
print(new_alphabet_translation("What's the Frequency, Kenneth?"))  # Output: \/\/[-]@'][''$ ']['[-]3 #|Z3(,)|_|3[]\[](`/, |<3[]\[][]\[]3']['[-]?
```
