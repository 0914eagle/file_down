
    if len(s0) != len(s1):
        return False
    else:
        for char in s0:
            if char not in s1:
                return False
        return True
 