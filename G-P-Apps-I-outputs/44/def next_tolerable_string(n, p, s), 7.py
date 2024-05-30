
def next_tolerable_string(n, p, s):
    s = list(s)
    for i in range(n-1, -1, -1):
        if ord(s[i]) - ord('a') == p - 1:
            s[i] = 'a'
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    else:
        print("NO")
        return
    
    for j in range(i+1, n):
        if s[j] == s[j-1]:
            if s[j] == chr(ord('a') + p - 1):
                s[j] = 'a'
            else:
                s[j] = chr(ord(s[j]) + 1)
        if j < n-1 and s[j] == s[j+1]:
            if s[j] == chr(ord('a') + p - 1):
                s[j] = 'a'
            else:
                s[j] = chr(ord(s[j]) + 1)
    
    print(''.join(s))

# Example usage
n, p = map(int, input().split())
s = input()
next_tolerable_string(n, p, s)
```
