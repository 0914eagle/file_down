
    vowels = 'aeiouAEIOU'
    new_text = ''
    for letter in text:
        if letter not in vowels:
            new_text += letter
    return new_text
 