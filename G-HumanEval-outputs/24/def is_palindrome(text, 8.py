
def is_palindrome(text: str):
    if text == text[::-1]:
        return True
    else:
        return False

print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
