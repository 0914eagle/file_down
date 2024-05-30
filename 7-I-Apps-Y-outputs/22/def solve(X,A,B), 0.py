
def solve(X,A,B):
    if X-A+1 <= B <= X:
        return "safe"
    elif B > X:
        return "dangerous"
    else:
        return "delicious"

