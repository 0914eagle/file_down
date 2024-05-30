
def mr_infinity_string(s, k):
    def next_day(s):
        new_s = ""
        for c in s:
            if c == '1':
                new_s += c
            else:
                new_s += c * int(c)
        return new_s

    days = 5 * 10**15
    while days > 0:
        s = next_day(s)
        days -= 1

    return s[k-1]

# Input
S, K = input().split()
K = int(K)

# Output
print(mr_infinity_string(S, K))
```
