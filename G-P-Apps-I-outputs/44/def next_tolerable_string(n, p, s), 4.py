
def next_tolerable_string(n, p, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_list = list(s)
    
    for i in range(n - 1, -1, -1):
        if s_list[i] != alphabet[p - 1]:
            current_char_idx = alphabet.index(s_list[i])
            next_char = alphabet[current_char_idx + 1]
            if i > 0 and next_char == s_list[i - 1]:
                next_char = alphabet[current_char_idx + 2]
            
            if next_char in alphabet[:p]:
                s_list[i] = next_char
                for j in range(i + 1, n):
                    if s_list[j - 1] == s_list[j]:
                        s_list[j] = alphabet[alphabet.index(s_list[j]) + 1]
                        if s_list[j] not in alphabet[:p]:
                            s_list[j] = alphabet[0]
                return ''.join(s_list)
    
    return "NO"

# Read input
n, p = map(int, input().split())
s = input()

# Get the next tolerable string
result = next_tolerable_string(n, p, s)
print(result)
```
