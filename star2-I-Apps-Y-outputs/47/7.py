
n = int(input())
s = input()

def isGood(s):
    if len(s) % 2 != 0:
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
    while i < len(s):
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
        else:
            i += 2
            
    print(len(s))
    print(s)

