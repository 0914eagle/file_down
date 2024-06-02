
def cycpattern_check(a , b):
    
    if len(a) < len(b):
        return False
    if a.find(b) != -1:
        return True
    for i in range(len(b)-1):
        b = b[-1] + b[:-1]
        if a.find(b) != -1:
            return True
    return False
 