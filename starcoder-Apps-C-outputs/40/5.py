
def heap(tree,cur):
    if cur>n:
        return 0
    l=heap(tree,cur*2)
    r=heap(tree,cur*2+1)
    if l==-1 or r==-1 or tree[cur]<=tree[cur*2] or tree[cur]<=tree[cur*2+1]:
        return -1
    return l+r+1
tree=[]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    tree.append(a)
print(heap(tree,1))
