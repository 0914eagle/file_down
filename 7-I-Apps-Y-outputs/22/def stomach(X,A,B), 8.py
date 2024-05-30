
def stomach(X,A,B):
    if A-B <= X:
        return "safe"
    elif A-B > X+1:
        return "dangerous"
    else:
        return "delicious"

