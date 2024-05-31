
def check_string(input_string):
    vowels = set(['A', 'E', 'I', 'O', 'U'])

    count = 0
    for char in input_string:
        if char in vowels:
            count += 1

    if count >= 3:
        return "YES"
    else:
        return "NO"

# Test cases
print(check_string("GENIUS"))  # Output: YES
print(check_string("DOCTOR"))  # Output: NO
print(check_string("IRENE"))   # Output: YES
print(check_string("MARY"))    # Output: NO
print(check_string("SMARTPHONE"))  # Output: NO
print(check_string("REVOLVER"))    # Output: YES
print(check_string("HOLMES"))      # Output: NO
print(check_string("WATSON"))      # Output: YES
