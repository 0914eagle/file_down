
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(0, len(s), 3):
        if s[i:i+3] == s[i+1:i+4] == s[i+2:i+5]:
            return False
    return True
 