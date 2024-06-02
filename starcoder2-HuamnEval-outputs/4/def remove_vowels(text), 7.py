
 def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = ''
    for i in text:
        if i not in vowels:
            result += i
    return result
 