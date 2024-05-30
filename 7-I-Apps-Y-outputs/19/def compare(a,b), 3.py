
def compare(a,b):
    a = str(a)
    b = str(b)
    return a[::-1] if int(a[::-1]) > int(b[::-1]) else b[::-1]

