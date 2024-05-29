
def is_nice_word(s):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if len(s) < 26:
        return -1
    
    for i in range(len(s) - 25):
        substring = s[i:i+26]
        question_marks = [char for char in substring if char == '?']
        letters = [char for char in substring if char in ALPHABET]

        if len(letters) + len(question_marks) < 26:
            continue
        
        filled_string = s[:i] + ALPHABET
        remaining_string = s[i+26:]
        filled_string += remaining_string.replace('?', 'A')  # Fill remaining missing letters with 'A'
        
        return filled_string

    return -1

# Example input
s = 'ABC??FGHIJK???OPQR?TUVWXY?'
output = is_nice_word(s)
print(output)
```
