
def make_good_string(n, s):
    i = 0
    res = []
    while i < len(s):
        res.append(s[i])
        if i+1 < len(s) and s[i] == s[i+1]:
            i += 1
        i += 1
    return len(s) - len(res), ''.join(res)

# Input parsing
n = int(input())
s = input().strip()

# Call the function and output the result
k, result = make_good_string(n, s)
print(k)
print(result)
```
