
def next_tolerable_string(n, p, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_list = list(s)
    
    for i in range(n-1, -1, -1):
        if alphabet.index(s_list[i]) < p-1:
            s_list[i] = alphabet[alphabet.index(s_list[i]) + 1]
            for j in range(i+1, n):
                s_list[j] = alphabet[0]
            if not any(s_list[i] == s_list[i+1] for i in range(n-1)):
                return "".join(s_list)
    
    return "NO"

# Input example
n, p = 4, 4
s = "abcd"
print(next_tolerable_string(n, p, s))
```
