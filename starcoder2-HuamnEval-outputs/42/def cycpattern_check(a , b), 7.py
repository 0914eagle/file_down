
 def cycpattern_check(a , b):
    
    if b in a:
        return True
    else:
        for i in range(len(a)-1):
            a = a[1:] + a[0]
            if b in a:
                return True
        return False
 