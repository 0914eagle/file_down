
def solve(P,boxes):
    # 递归函数
    def dfs(index,p,e):
        # 如果已经找到
        if p>=P:
            return e
        # 已经搜索完所有盒子
        if index==n:
            return inf
        # 不搜索当前盒子
        r1=dfs(index+1,p,e)
        # 搜索当前盒子
        r2=dfs(index+1,p*boxes[index][1],e+boxes[index][0])
        # 选取两种方式搜索结果中最小值
        return min(r1,r2)
    # 搜索的结果
    inf=float('inf')
    # 盒子数
    n=len(boxes)
    # 递归
    result=dfs(0,1,0)
    # 如果可以搜索所有盒子
    if result==inf:
        # 输出-1
        print(-1)
    # 否则输出搜索的结果
    else:
        print(int(result))

# 盒子数
n=int(input())
# 要保证的最低概率
P=float(input())
# 盒子
boxes=[]
# 输入所有盒子信息
for i in range(n):
    e,p=map(float,input().split())
    # 盒子
    boxes.append((e,p))
# 解决问题
solve(P,boxes)
