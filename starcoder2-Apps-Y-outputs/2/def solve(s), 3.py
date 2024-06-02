
def solve(s):
    return ''.join(c for c in s if c != 'B' or not s.pop())

s = input()
print(solve(list(s)))

