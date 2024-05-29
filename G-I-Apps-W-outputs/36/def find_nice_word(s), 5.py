
def find_nice_word(s):
    if len(s) < 26:
        return -1
    
    for i in range(len(s) - 25):
        substring = s[i:i+26]
        unique_chars = set()
        missing_chars = []
        
        for char in substring:
            if char != '?' and char in unique_chars:
                break
            if char != '?':
                unique_chars.add(char)
            else:
                missing_chars.append(char)
        
        if len(unique_chars) + len(missing_chars) == 26:
            replacement_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - unique_chars
            nice_word = list(substring)
            for j in range(26):
                if nice_word[j] == '?':
                    nice_word[j] = replacement_chars.pop()
            filled_word = s[:i] + ''.join(nice_word) + s[i+26:]
            return filled_word
            
    return -1

# Input example
s = "ABC??FGHIJK???OPQR?TUVWXY?"
result = find_nice_word(s)
print(result)
```
