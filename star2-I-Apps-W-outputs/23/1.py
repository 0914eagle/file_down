
def is_quasi_palindromic(x):
    s = str(x)
    return s == s[::-1]

x = int(input())
print("YES" if is_quasi_palindromic(x) else "NO")

