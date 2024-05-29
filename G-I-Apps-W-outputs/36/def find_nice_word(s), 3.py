
from string import ascii_uppercase

def find_nice_word(s):
    if len(s) < 26:
        return -1

    for i in range(len(s) - 25):
        sub = s[i:i+26]
        missing_chars = [char for char in ascii_uppercase if char not in sub and char != '?']
        
        if len(missing_chars) <= s.count('?'):
            nice_word = ''
            replaced_chars = 0
            for char in s:
                if char == '?':
                    if replaced_chars < len(missing_chars):
                        nice_word += missing_chars[replaced_chars]
                        replaced_chars += 1
                    else:
                        nice_word += 'X'  # Any filler character
                else:
                    nice_word += char

            return nice_word

    return -1

s = input()
print(find_nice_word(s))
```
