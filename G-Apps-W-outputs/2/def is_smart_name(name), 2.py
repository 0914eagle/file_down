
def is_smart_name(name):
    vowels = "AEIOU"
    count_vowels = 0
    count_consonants = 0
    
    for letter in name:
        if letter in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
    
    return "YES" if count_vowels > count_consonants else "NO"

# Test cases
print(is_smart_name("GENIUS"))  # YES
print(is_smart_name("DOCTOR"))  # NO
print(is_smart_name("IRENE"))   # YES
print(is_smart_name("MARY"))    # NO
print(is_smart_name("SMARTPHONE"))  # NO
print(is_smart_name("REVOLVER"))    # YES
print(is_smart_name("HOLMES"))      # NO
print(is_smart_name("WATSON"))      # YES
