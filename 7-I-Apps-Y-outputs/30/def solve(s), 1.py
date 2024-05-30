
def solve(s):
    n = len(s)
    if n % 3 == 0:
        return s
    elif n % 3 == 1:
        return s[:n//3] + '0' + s[n//3+1:]
    else:
        return s[:n//3] + '2' + s[n//3+1:]


s = input()
print(solve(s))

