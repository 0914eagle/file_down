
def next_tolerable_string(n, p, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_list = list(s)
    
    for i in range(n-1, -1, -1):
        if s_list[i] != alphabet[p-1]:
            s_list[i] = alphabet[alphabet.index(s_list[i])+1]
            break
        else:
            s_list[i] = alphabet[0]
    
    for j in range(i+1, n):
        if s_list[j] == s_list[j-1]:
            s_list[j] = alphabet[(alphabet.index(s_list[j])+1)%p]
    
    next_tolerable = ''.join(s_list)
    
    for k in range(1, n):
        if next_tolerable[k] == next_tolerable[k-1]:
            return "NO"
    
    return next_tolerable

# Input example
n, p = 4, 4
s = 'abcd'
print(next_tolerable_string(n, p, s))
