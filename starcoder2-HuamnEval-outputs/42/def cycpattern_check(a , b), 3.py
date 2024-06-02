
def cycpattern_check(a , b):
    
    if len(b) > len(a):
        return False
    else:
        for i in range(len(a)):
            if a[i:].startswith(b):
                return True
        return False
 