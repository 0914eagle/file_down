
def is_quasi_palindrome(x):
    s = str(x)
    return s == s[::-1]

x = int(input())
print("YES" if is_quasi_palindrome(x) else "NO")

