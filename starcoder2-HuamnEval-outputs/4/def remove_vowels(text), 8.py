
 def remove_vowels(text):
    
    vowels = 'aeiouAEIOU'
    text_without_vowels = ''
    for char in text:
        if char not in vowels:
            text_without_vowels += char
    return text_without_vowels
 