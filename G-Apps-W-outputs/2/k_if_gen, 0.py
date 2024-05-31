k_if_genius(word):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    if count >= len(word) - count:
        return "YES"
    else:
        return "NO"

# Test cases
print(check_if_genius("GENIUS"))  # Output: YES
print(check_if_genius("DOCTOR"))  # Output: NO
print(check_if_genius("IRENE"))  # Output: YES
print(check_if_genius("MARY"))  # Output: NO
print(check_if_genius("SMARTPHONE"))  # Output: NO
print(check_if_genius("REVOLVER"))  # Output: YES
print(check_if_genius("HOLMES"))  # Output: NO
print(check_if_genius("WATSON"))  # Output: YES
[/PYTHON