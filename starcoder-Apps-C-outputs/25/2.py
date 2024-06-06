
import numpy as np

def calc(nr,nc,n,m,delete,keep,if_move):
    if n==0:
        return 0
    elif m==0:
        return 0
    elif if_move==0:
        return -1
    delete=np.array(delete)
    keep=np.array(keep)
    delete_sort=np.sort(delete,axis=0)
    keep_sort=np.sort(keep,axis=0)
    ans=1000000
    for i in range(m):
        r_min=max(0,keep_sort[i][0]-15)
        r_max=min(keep_sort[i][0]+15,nr-15)
        c_min=max(0,keep_sort[i][1]-9)
        c_max=min(keep_sort[i][1]+9,nc-9)
        for r in range(r_min,r_max+1):
            for c in range(c_min,c_max+1):
                ans1=0
                for j in range(n):
                    if delete_sort[j][0]<r or (delete_sort[j][0]==r and delete_sort[j][1]<c):
                        ans1+=1
                for j in range(i):
                    if keep_sort[j][0]<r or (keep_sort[j][0]==r and keep_sort[j][1]<c):
                        ans1+=1
                if ans1<ans:
                    ans=ans1
    return ans

if __name__=="__main__":
    nr,nc,n,m=map(int,input().split())
    delete=[]
    keep=[]
    for i in range(n+m):
        r,c=map(int,input().split())
        if i<n:
            delete.append([r,c])
        else:
            keep.append([r,c])
    print(calc(nr,nc,n,m,delete,keep,1))
