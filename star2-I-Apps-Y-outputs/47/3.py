
n = int(input())
s = input()

def is_good(s):
    if len(s) % 2 == 1:
        return False
    
    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            return False
    
    return True

if is_good(s):
    print(0)
    print(s)
else:
    i = 0
    while not is_good(s):
        s = s[:i] + s[i+1:]
        i += 1
    
    print(len(s) - len(s.lstrip()))
    print(s.lstrip())

