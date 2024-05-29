
def find_nice_word(s):
    if len(s) < 26:
        return -1

    for i in range(len(s) - 25):
        temp = set()
        missing_chars = []
        for j in range(26):
            if s[i+j] == '?':
                missing_chars.append(j)
            else:
                temp.add(s[i+j])

        if len(temp) + len(missing_chars) == 26:
            all_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            available_letters = all_letters - temp
            for k in range(26):
                if s[i+k] == '?':
                    s = s[:i+k] + available_letters.pop() + s[i+k+1:]

            return s

    return -1

s = input().strip()
result = find_nice_word(s)
print(result)
```
