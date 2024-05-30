
def mr_infinity_string(s, k):
    days = 5 * 10 ** 15

    while days > 0:
        new_s = ''
        for digit in s:
            if digit == '1':
                new_s += '1'
            else:
                new_s += digit * int(digit)

        s = new_s
        days -= 1

    return s[k - 1]

# Read input
s, k = input().split()
k = int(k)

# Output the K-th character from the left in the string after 5 * 10^15 days
print(mr_infinity_string(s, k))
```
