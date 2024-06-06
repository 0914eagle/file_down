
def find(A, s):
    for a in A:
        if s & a:
            return a
    return None
