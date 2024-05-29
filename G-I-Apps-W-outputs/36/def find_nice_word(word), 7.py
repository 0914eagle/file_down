
def find_nice_word(word):
    if len(word) < 26:
        return -1

    for i in range(len(word) - 25):
        unique_chars = set()
        missing_chars = []
        nice_substr = True
        
        for j in range(i, i+26):
            if word[j] != '?' and word[j] in unique_chars:
                nice_substr = False
                break
            elif word[j] == '?':
                missing_chars.append(j)
            else:
                unique_chars.add(word[j])
        
        if nice_substr:
            available_chars = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if char not in unique_chars]
            if len(available_chars) >= len(missing_chars):
                for k in range(len(missing_chars)):
                    word = word[:missing_chars[k]] + available_chars[k] + word[missing_chars[k]+1:]
                return word.replace('?', 'A')
    
    return -1

# Input
s = input().strip()

# Output
result = find_nice_word(s)
print(result)
```
