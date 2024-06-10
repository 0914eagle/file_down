
n = int(input())
s = input()

def is_good(s):
    if len(s) == 0:
        return True
    
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]:
            return False
    
    return True
    
def solve(s):
    if is_good(s):
        return 0
    
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]
        
        if is_good(new_s):
            return 1
    
    return 2
    
print(solve(s))

