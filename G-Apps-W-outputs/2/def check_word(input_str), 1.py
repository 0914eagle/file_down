
def check_word(input_str):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    for char in input_str:
        if char in vowels:
            return "YES"
    
    return "NO"

# Test cases
print(check_word("GENIUS"))  # Output: YES
print(check_word("DOCTOR"))  # Output: NO
print(check_word("IRENE"))   # Output: YES
print(check_word("MARY"))    # Output: NO
print(check_word("SMARTPHONE"))  # Output: NO
print(check_word("REVOLVER"))   # Output: YES
print(check_word("HOLMES"))     # Output: NO
print(check_word("WATSON"))     # Output: YES
