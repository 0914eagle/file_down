
 def remove_vowels(text):
    
    vowels = 'aeiouAEIOU'
    new_text = ''
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text
 