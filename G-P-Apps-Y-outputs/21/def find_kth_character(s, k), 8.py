
def find_kth_character(s, k):
    n = len(s)
    days = 5 * 10**15

    while days > 0:
        new_s = ""
        for char in s:
            if char != '1':
                new_s += char * int(char)
            else:
                new_s += char
        s = new_s
        days -= 1

    return s[k-1]

# Input
s = input().strip()
k = int(input().strip())

# Output
print(find_kth_character(s, k))
```
