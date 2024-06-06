
n = int(input())
s = input()

def is_happy(s):
    if len(s) == 0:
        return True
    if len(s) % 2 == 1:
        return False
    l = len(s) // 2
    return is_happy(s[:l]) and is_happy(s[l:])

def solve(s):
    if is_happy(s):
        return 'Bicarp'
    if len(s) == 0:
        return 'Monocarp'
    if s[0] == '?':
        for i in range(10):
            if solve(str(i) + s[1:]) == 'Bicarp':
                return 'Monocarp'
        return 'Bicarp'
    return solve(s[1:])

print(solve(s))
