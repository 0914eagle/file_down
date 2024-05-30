
def animal(b,d,c,l):
    if l%4==0:
        if b*4+d*4+c*4==l:
            print(b,d,c)
        else:
            print("impossible")
    else:
        print("impossible")

