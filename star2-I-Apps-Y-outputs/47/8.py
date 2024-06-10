
n = int(input())
s = input()

def isGood(s):
    if len(s) % 2 == 1:
        return False
    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            return False
    return True

if isGood(s):
    print(0)
    print(s)
else:
    i = 0
    while not isGood(s):
        s = s[:i] + s[i+1:]
        i += 1
    print(len(s) - n)
    print(s)

