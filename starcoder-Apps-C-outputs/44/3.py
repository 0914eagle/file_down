
def main():
    [x0,y0,ax,ay,bx,by] = map(int,input().split())
    [xs,ys,t] = map(int,input().split())
    print(node(x0,y0,ax,ay,bx,by,xs,ys,t))

def node(x0,y0,ax,ay,bx,by,xs,ys,t):
    s=set([(x0,y0)])
    x=x0
    y=y0
    t=t-2
    while t>0:
        x=ax*x+bx
        y=ay*y+by
        if (x,y) not in s:
            s.add((x,y))
            t-=2
    return len(s)
main()
