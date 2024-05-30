
def next_day(s):
    new_s = ""
    for char in s:
        if char == '1':
            new_s += '1'
        else:
            new_s += char * int(char)
    return new_s

def kth_char_after_days(s, k, days):
    for _ in range(days):
        s = next_day(s)
    return s[k-1]

# Input processing
S = input().strip()
K = int(input())

# Calculate the result after 5 * 10^15 days
result = kth_char_after_days(S, K, 5 * 10**15)
print(result)
```
