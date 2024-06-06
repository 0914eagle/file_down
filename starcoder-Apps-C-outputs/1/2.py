
def digit(x):
    s=0
    while x>0:
        s+=x%10
        x=x//10
    return s

def f(x):
    if x<10:
        return x
    else:
        return f(digit(x))

def g(a,b):
    if a==b:
        return f(a)
    elif a==0:
        a=10
    elif b==0:
        b=10
    else:
        pass
    res=[]
    for i in range(10):
        res.append(0)
    for i in range(a,b):
        res[f(i)]+=1
    return res

def main():
    x,y=map(int,input().split())
    res=g(x,y+1)
    for i in range(10):
        print(res[i],end=' ')
main()
