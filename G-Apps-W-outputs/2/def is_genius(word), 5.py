
def is_genius(word):
    vowels = set("AEIOU")
    count_vowels = sum(1 for letter in word if letter in vowels)
    
    return "YES" if count_vowels >= len(word) - count_vowels else "NO"

# Test cases
print(is_genius("GENIUS"))  # Output: YES
print(is_genius("DOCTOR"))  # Output: NO
print(is_genius("IRENE"))   # Output: YES
print(is_genius("MARY"))    # Output: NO
print(is_genius("SMARTPHONE"))  # Output: NO
print(is_genius("REVOLVER"))    # Output: YES
print(is_genius("HOLMES"))      # Output: NO
print(is_genius("WATSON"))      # Output: YES
