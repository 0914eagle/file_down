
def new_alphabet_translation(text):
    translation_dict = {
        'a': '@', 'n': '[]\[]', 'b': '8', 'o': '0', 'c': '(', 'p': '|D',
        'd': '|)', 'q': '(,)', 'e': '3', 'r': '|Z', 'f': '#', 's': '$',
        'g': '6', 't': '\'][\'', 'h': '[-]', 'u': '|_|', 'i': '|', 'v': '\/',
        'j': '_|', 'w': '\/\/', 'k': '|<', 'x': '}{', 'l': '1', 'y': '`/',
        'm': '[]\/[]', 'z': '2', 'A': '@', 'N': '[]\[]', 'B': '8', 'O': '0',
        'C': '(', 'P': '|D', 'D': '|)', 'Q': '(,)', 'E': '3', 'R': '|Z', 'F': '#',
        'S': '$', 'G': '6', 'T': '\'][\'', 'H': '[-]', 'U': '|_|', 'I': '|',
        'V': '\/', 'J': '_|', 'W': '\/\/', 'K': '|<', 'X': '}{', 'L': '1', 'Y': '`/',
        'M': '[]\/[]', 'Z': '2'
    }

    new_text = ''
    for char in text:
        if char in translation_dict:
            new_text += translation_dict[char]
        else:
            new_text += char

    return new_text

# Example usage
input_text = "All your base are belong to us."
output_text = new_alphabet_translation(input_text)
print(output_text)
```
