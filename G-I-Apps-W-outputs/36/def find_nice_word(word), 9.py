
def find_nice_word(word):
    if len(word) < 26:
        return -1
    
    alphabet_set = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    for i in range(len(word) - 25):
        substring = word[i:i+26]
        missing_chars = [char for char in alphabet_set if char not in substring and char != '?']
        question_marks = [index for index, char in enumerate(substring) if char == '?']
        
        if len(missing_chars) <= len(question_marks):
            possible_word = list(substring)
            for j in range(len(missing_chars)):
                possible_word[question_marks[j]] = missing_chars[j]
            
            for k in range(len(possible_word)):
                if possible_word[k] == '?':
                    possible_word[k] = next(iter(alphabet_set - set(possible_word)))
                    
            return ''.join(possible_word)
    
    return -1

# Input example
word = "ABC??FGHIJK???OPQR?TUVWXY?"

result = find_nice_word(word)
print(result)
```
