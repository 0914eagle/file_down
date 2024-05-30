
def kth_char_after_days(S, K):
    def calculate_next_day(string):
        new_string = ''
        for char in string:
            if char == '1':
                new_string += char
            else:
                new_string += char * int(char)
        return new_string

    days = 5 * 10**15
    while days > 0:
        S = calculate_next_day(S)
        days -= 1

    return S[K-1]

# Read input
S, K = input().split()
K = int(K)

# Call the function and print the result
print(kth_char_after_days(S, K))
```
