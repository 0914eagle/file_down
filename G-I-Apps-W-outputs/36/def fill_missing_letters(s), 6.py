
def fill_missing_letters(s):
    if len(s) < 26:
        return -1

    for i in range(len(s) - 26 + 1):
        substring = s[i:i+26]
        letters = set()
        question_marks = []
        
        for j in range(26):
            if substring[j] == '?':
                question_marks.append(j)
            else:
                letters.add(substring[j])

        missing_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - letters
        if len(missing_letters) == len(question_marks):
            result = list(substring)
            for k, missing_letter in zip(question_marks, missing_letters):
                result[k] = missing_letter
            for l in range(i):
                if result[l] == '?':
                    result[l] = 'A'
            for m in range(i+26, len(s)):
                if result[m] == '?':
                    result[m] = 'A'
            return ''.join(result)
    
    return -1

s = input().strip()
print(fill_missing_letters(s))
```
