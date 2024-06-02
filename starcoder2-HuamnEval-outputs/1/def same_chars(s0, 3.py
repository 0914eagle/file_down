
def same_chars(s0: str, s1: str):
    
    s0 = ''.join(sorted(s0))
    s1 = ''.join(sorted(s1))
    return s0 == s1
