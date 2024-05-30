
def next_tolerable_string(n, p, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_list = list(s)
    for i in range(n - 1, -1, -1):
        s_list[i] = alphabet[alphabet.index(s_list[i]) + 1]
        if s_list[i] not in alphabet[:p]:
            s_list[i] = alphabet[alphabet.index(s_list[i]) - p + 1]
        else:
            break
    else:
        return "NO"

    for j in range(i + 1, n):
        s_list[j] = alphabet[0]
        if j > 0 and s_list[j] == s_list[j - 1]:
            s_list[j] = alphabet[1]

    return ''.join(s_list)

# Input
n, p = map(int, input().split())
s = input().strip()

# Output
result = next_tolerable_string(n, p, s)
print(result)
```
