
def is_palindrome(a):
    return a == a[::-1]

def has_palindrome(a):
    for i in range(len(a) - 2):
        for j in range(i + 3, len(a) + 1):
            if is_palindrome(a[i:j]):
                return True
    return False

def solve(n, a):
    if has_palindrome(a):
        return "YES"
    return "NO"

