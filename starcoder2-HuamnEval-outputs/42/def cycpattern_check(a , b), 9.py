
def cycpattern_check(a , b):
    
    if b in a:
        return True
    else:
        for i in range(len(a)):
            a = a[-1] + a[:-1]
            if b in a:
                return True
    return False
 