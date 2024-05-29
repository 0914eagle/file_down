
def find_nice_word(s):
    if len(s) < 26:
        return -1

    for i in range(len(s) - 25):
        substring = s[i:i+26]
        unique_chars = set(substring.replace('?', ''))
        
        if len(unique_chars) + substring.count('?') == 26 and len(unique_chars) == 26:
            nice_word = list(s)
            for j in range(26):
                if nice_word[i + j] == '?':
                    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if char not in unique_chars:
                            nice_word[i + j] = char
                            unique_chars.add(char)
                            break
            for k in range(len(s)):
                if nice_word[k] == '?':
                    nice_word[k] = 'A'
            return ''.join(nice_word)
    
    return -1

# Input
s = input().strip()

# Output
result = find_nice_word(s)
print(result)
```
