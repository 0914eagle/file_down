
def make_string_good(n, s):
    res = []
    prev_char = ''
    count = 0
    for char in s:
        if char != prev_char:
            res.append(char)
            prev_char = char
        else:
            count += 1
    if len(res) % 2 != 0:
        res.pop()
        count += 1
    return count, ''.join(res)

# Input
n = int(input())
s = input().strip()

# Output
count, result = make_string_good(n, s)
print(count)
print(result)
```
