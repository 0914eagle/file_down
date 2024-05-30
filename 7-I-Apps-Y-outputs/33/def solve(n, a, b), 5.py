
def solve(n, a, b):
    # Write your code here
    if n < a:
        return
    if n == a:
        return 'a' * n
    if a == 1:
        return 'a' * n
    if b == 1:
        return 'a' * n
    if b == 26:
        return 'a' * n
    if n % a != 0:
        return 'a' * (n % a) + 'b' * (n // a - 1) * a
    if n % a == 0:
        return 'a' * n


