
 def is_palindrome(text: str):
    
    if len(text) < 2:
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False
