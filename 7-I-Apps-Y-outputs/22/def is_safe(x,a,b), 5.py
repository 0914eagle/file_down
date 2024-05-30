
def is_safe(x,a,b):
    if a-b <= x:
        return "safe"
    elif a-b <= x+1:
        return "delicious"
    else:
        return "dangerous"

