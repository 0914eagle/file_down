
from math import *
def main():
    input()
    array=[]
    for i in input().split(' '):
        array.append(int(i))
    lena=len(array)
    time=int(sqrt(lena))
    ans=[]
    for i in range(time):
        maxa=array[time*i]
        for j in range(time):
            if(array[time*i+j]>maxa):
                maxa=array[time*i+j]
        ans.append(maxa)
    ans.append(max(array[time*time:]))
    print(ans)
if __name__=='__main__':
    main()
