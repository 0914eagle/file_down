
def solve(n, a, b):
    # Fill this in.
    if n < a:
        return ""
    if a == 1 and b == 1:
        return "a" * n
    if a == 1 and b > 1:
        return "a" * n
    if a > 1 and b == 1:
        return "a" * n
    if a > 1 and b > 1:
        return "a" * (n // a) + "b" * (n % a)

