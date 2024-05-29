
def make_string_good(n, s):
    odd_chars = set()
    
    for i in range(1, len(s), 2):
        if s[i] == s[i-1]:
            odd_chars.add(s[i])
    
    chars_to_delete = []
    result = []
    
    for i, char in enumerate(s):
        if i % 2 == 0 or char not in odd_chars:
            result.append(char)
        else:
            chars_to_delete.append(char)
    
    return len(chars_to_delete), ''.join(result)

# Input processing
n = int(input())
s = input()

k, new_s = make_string_good(n, s)
print(k)
print(new_s)
```
