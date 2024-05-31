
def check_vowels_consonants(input_string):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    consonants = set('BCDFGHJKLMNPQRSTVWXYZ')

    vowel_count = sum(1 for letter in input_string if letter in vowels)
    consonant_count = sum(1 for letter in input_string if letter in consonants)

    if vowel_count > consonant_count:
        return "YES"
    else:
        return "NO"

# Test cases
print(check_vowels_consonants("GENIUS"))  # Output: YES
print(check_vowels_consonants("DOCTOR"))  # Output: NO
print(check_vowels_consonants("IRENE"))   # Output: YES
print(check_vowels_consonants("MARY"))    # Output: NO
print(check_vowels_consonants("SMARTPHONE"))  # Output: NO
print(check_vowels_consonants("REVOLVER"))   # Output: YES
print(check_vowels_consonants("HOLMES"))     # Output: NO
print(check_vowels_consonants("WATSON"))     # Output: YES
