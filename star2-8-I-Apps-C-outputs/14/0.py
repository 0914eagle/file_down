
r,c,k,l=map(int,input().split())
x0,y0=map(int,input().split())
t=[]
for i in range(r):
  t.append(list(map(int,input().split())))

class Graph:
  def __init__(self,t,k,l):
    self.t=t
    self.k=k
    self.l=l
    self.r=len(t)
    self.c=len(t[0])
    self.visited=[[False for i in range(self.c)] for j in range(self.r)]
    self.adj_list=[[] for i in range(self.r*self.c)]
    for x in range(self.r):
      for y in range(self.c):
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
          if 0<=x+i<self.r and 0<=y+j<self.c and self.t[x][y]<=self.l and self.t[x+i][y+j]<=self.l:
            self.adj_list[x*self.c+y].append((x+i)*self.c+y+j)
  def dfs(self,pos):
    self.visited[pos//self.c][pos%self.c]=True
    count=1
    for i in self.adj_list[pos]:
      if self.visited[i//self.c][i%self.c]==False:
        count+=self.dfs(i)
    return count
g=Graph(t,k,l)
print(g.dfs(x0*c+y0))

