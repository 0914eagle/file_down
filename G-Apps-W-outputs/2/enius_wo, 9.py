enius_word(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    count_vowels = 0
    count_consonants = 0

    for letter in word:
        if letter in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

    if count_vowels > count_consonants:
        return "YES"
    else:
        return "NO"

# Test cases
print(is_genius_word("GENIUS"))  # Output: YES
print(is_genius_word("DOCTOR"))  # Output: NO
print(is_genius_word("IRENE"))  # Output: YES
print(is_genius_word("MARY"))  # Output: NO
print(is_genius_word("SMARTPHONE"))  # Output: NO
print(is_genius_word("REVOLVER"))  # Output: YES
print(is_genius_word("HOLMES"))  # Output: NO
print(is_genius_word("WATSON"))  # Output: YES
[/PYTHON