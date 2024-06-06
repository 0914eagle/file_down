
def sherlock_and_door(n,m,r_list,lock_list):
    for i in range(m):
        for j in range(len(lock_list[i])):
            r_list[lock_list[i][j]-1]=(r_list[lock_list[i][j]-1]+1)%2
    if sum(r_list)==n:
        return 'YES'
    return 'NO'

n,m=[int(i) for i in input().split()]
r_list=[int(i) for i in input().split()]
lock_list=[]
for i in range(m):
    lock_list.append([int(i) for i in input().split()])
print(sherlock_and_door(n,m,r_list,lock_list))
