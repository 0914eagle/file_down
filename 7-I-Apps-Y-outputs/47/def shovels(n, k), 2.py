
def shovels(n, k):
    if n == 1:
        return 1
    if n < 1:
        return 0
    if n % k == 0:
        return n // k
    else:
        return (n // k) + 1

