
def takahashi_and_aoki(A,B,C,D):
    while A>0 and C>0:
        if A>C:
            C-=B
        else:
            A-=D
    return "Yes" if A<=0 else "No"

