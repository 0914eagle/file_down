
def read_file(n,f):
    answer=0
    pos=0
    for i in range(n):
        answer=answer+abs(pos-f[i])
        pos=f[i]
    print(answer)
n=int(input())
f=list(map(int,input().split()))
read_file(n,f)
