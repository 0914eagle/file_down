
def main():
    n,g = map(int,input().split())
    list=[]
    for i in range(n):
        list.append(list(map(int,input().split())))
    list=sorted(list,key=lambda x:x[0])
    list=sorted(list,key=lambda x:x[1])
    total=0
    num=0
    for i in range(n):
        if list[i][1]*(list[i][0]-num)>g:
            return print('cancel road trip')
        if list[i][1]*(list[i][0]-num)<=g:
            total+=list[i][1]*(list[i][0]-num)
            num=list[i][0]
    return print(total)
main()
