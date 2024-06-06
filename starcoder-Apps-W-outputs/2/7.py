
from collections import defaultdict
n,h,m,k = map(int,input().split())
trains = []
for i in range(n):
    trains.append(list(map(int,input().split())))

if(k > m//2):
    print(0,0)
else:
    l = []
    d = defaultdict(int)
    for i in range(n):
        time = trains[i][0]*60 + trains[i][1]
        x = time % m
        y = (time + k) % m
        if(x >= k and x <= m-k):
            l.append(trains[i])
        else:
            if(k > x):
                d[m-y] += 1
            else:
                d[y] += 1
    
    if(len(l) == n):
        print(0,0)
        exit(0)
    else:
        trains = []
        for key, value in sorted(d.items(), reverse=True):
            trains.extend([key]*value)
        print(n-len(l),trains[0])
        for i in range(len(l)):
            print(i+1,end=' ')
