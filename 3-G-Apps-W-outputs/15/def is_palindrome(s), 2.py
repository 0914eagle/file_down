
def is_palindrome(s):
    return s == s[::-1]

def rearrange_string(s):
    if is_palindrome(s):
        return -1
    else:
        sorted_s = sorted(s)
        return ''.join(sorted_s)

t = int(input())
for _ in range(t):
    s = input().strip()
    result = rearrange_string(s)
    print(result)
