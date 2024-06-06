
# 题目大意：
# 给定三种类型的计算机，分别有a,b,c台，分别对应USB,PS/2,USB+PS/2三种接口，
# 给定m种鼠标，每种鼠标都有USB,PS/2两种接口，并且每种鼠标都有价格，
# 问如何购买鼠标，使得能给最多的计算机配上鼠标，并且在能给最多的计算机配上鼠标的前提下，使得花费的钱最少。

# 思路：
# 先对所有鼠标按照价格从小到大排序，然后依次遍历，如果当前鼠标能给USB接口的计算机配上，则给USB接口的计算机配上，
# 否则如果当前鼠标能给PS/2接口的计算机配上，则给PS/2接口的计算机配上，
# 否则如果当前鼠标能给USB+PS/2接口的计算机配上，则给USB+PS/2接口的计算机配上，
# 最后输出能给最多的计算机配上鼠标的数量和花费的钱数。

n,m=map(int,input().split())
a,b,c=map(int,input().split())

mouses=[]
for i in range(m):
    mouses.append(list(map(str,input().split())))

mouses.sort(key=lambda x:int(x[0]))

ans=0
cost=0
for i in range(m):
    if a>0 and mouses[i][1]=='USB':
        a-=1
        ans+=1
        cost+=int(mouses[i][0])
    elif b>0 and mouses[i][1]=='PS/2':
        b-=1
        ans+=1
        cost+=int(mouses[i][0])
    elif c>0 and mouses[i][1]=='USB+PS/2':
        c-=1
        ans+=1
        cost+=int(mouses[i][0])

print(ans,cost)
