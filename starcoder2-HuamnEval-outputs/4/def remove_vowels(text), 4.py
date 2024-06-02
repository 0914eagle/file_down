
 def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = list(text)
    for i in range(len(text)):
        if text[i] in vowels:
            text[i] = ''
    text = ''.join(text)
    return text
 