
#先把书按高度从高到低排序，这样求面积就是取前3本书的高度与3本书的宽度之和

def fun(h,t,n):
    h.sort()
    h.reverse()
    t.sort()
    print(max(h[:3])*sum(t))

n=int(input())
h=[]
t=[]
for i in range(n):
    a,b=map(int,input().split())
    h.append(a)
    t.append(b)
fun(h,t,n)
