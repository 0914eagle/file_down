
def fill_missing_letters(word):
    if len(word) < 26:
        return -1

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(len(word) - 25):
        sub = word[i:i+26]
        missing_letters = set()
        has_question_mark = False
        
        for j in range(26):
            if sub[j] == "?":
                has_question_mark = True
            else:
                missing_letters.add(sub[j])
        
        if len(missing_letters) + sub.count("?") == 26:
            filled_sub = list(sub)
            for j in range(26):
                if filled_sub[j] == "?":
                    for letter in alphabet:
                        if letter not in missing_letters:
                            filled_sub[j] = letter
                            missing_letters.add(letter)
                            break
            result = list(word)
            result[i:i+26] = filled_sub
            return "".join(result)
    
    return -1

# Test cases
word1 = "ABC??FGHIJK???OPQR?TUVWXY?"
word2 = "WELCOMETOCODEFORCESROUNDTHREEHUNDREDANDSEVENTYTWO"
word3 = "??????????????????????????"
word4 = "AABCDEFGHIJKLMNOPQRSTUVW??M"

print(fill_missing_letters(word1))
print(fill_missing_letters(word2))
print(fill_missing_letters(word3))
print(fill_missing_letters(word4))
```
