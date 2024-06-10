
def solve(s):
    missing = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if c not in s]
    if len(missing) > 0:
        for i in range(len(s)):
            if s[i] == '?':
                s = s[:i] + missing[0] + s[i+1:]
                missing = missing[1:]
                if len(missing) == 0:
                    break
    if len(missing) > 0:
        return -1
    return s

s = input()
print(solve(s))

