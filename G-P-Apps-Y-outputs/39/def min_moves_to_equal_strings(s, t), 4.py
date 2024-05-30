
def min_moves_to_equal_strings(s, t):
    len_s = len(s)
    len_t = len(t)
    
    if s == t:
        return 0
    
    if len_s == 0 or len_t == 0:
        return len_s + len_t
    
    min_moves = min(len_s, len_t)
    for i in range(min_moves):
        if s[-1] == t[-1]:
            s = s[:-1]
            t = t[:-1]
        else:
            break
        
    return len_s + len_t - 2*len(s)

# Reading input
s = input().strip()
t = input().strip()
print(min_moves_to_equal_strings(s, t))
```
