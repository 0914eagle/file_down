
 def remove_vowels(text):
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in vowels:
        text = text.replace(i, '')
    return text
 