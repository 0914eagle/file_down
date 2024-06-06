
#把一天分成十分钟，定义一个10*10 的数组，代表海的高度，
#把每隔一段时间都算出来，然后每个10*10的格子都走一遍，从最高点开始，
#找到它的最低点，那个点就是距离最远的点。
import math
a,m=map(float,input().split())
W,H,X,Y=map(int,input().split())
maps=[]
for i in range(H):
    maps.append(list(map(int,input().split())))

step=m/600
pos=[X*10,Y*10]
for i in range(int(12/step)):
    t=0.5*a*(math.cos(2*math.pi*i*step/12)+1)
    for x in range(W):
        for y in range(H):
            for p in range(10):
                for q in range(10):
                    h=maps[y][x]+t
                    if (x*10+p-pos[0])**2+(y*10+q-pos[1])**2>=(x*10-pos[0])**2+(y*10-pos[1])**2:
                        pos[0],pos[1]=x*10+p,y*10+q

print((pos[0]-X*10)**2+(pos[1]-Y*10)**2)

