
def is_palindrome(text: str):
    return text == text[::-1]

# Testing the function
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
