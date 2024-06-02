
def solve(s):
    n = len(s)
    if n == 1:
        return 0
    if s[0] == s[-1]:
        return 1
    return 0

s = input()
print(solve(s))

