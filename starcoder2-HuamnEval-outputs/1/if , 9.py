
    if len(s0) != len(s1):
        return False
    for c in s0:
        if c not in s1:
            return False
    return True
