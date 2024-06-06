
a=input()
a=list(a)
if '1' in a and '6' in a and '8' in a and '9' in a:
    a.sort()
    ans=int("".join(a))
    if ans%7==0:
        print(ans)
    else:
        print(0)
else:
    print(0)
