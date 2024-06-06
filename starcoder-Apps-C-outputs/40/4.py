
class Node:
    def __init__(self,val,parent,children,count):
        self.val=val
        self.parent=parent
        self.children=children
        self.count=count
class Solution:
    def largest_heap(self,root:Node):
        if not root:
            return 0
        if len(root.children)==0:
            return 1
        ans=1
        for child in root.children:
            ans+=self.largest_heap(child)
        return ans
    def max_heap(self,root:Node):
        if not root:
            return 0
        ans=0
        for child in root.children:
            if root.val>child.val:
                ans+=self.max_heap(child)
            else:
                ans+=self.largest_heap(child)
        return ans+1
if __name__=="__main__":
    n=int(input())
    nodes=[Node(-1,-1,[],1) for _ in range(n)]
    for i in range(n):
        v,p=map(int,input().strip().split())
        nodes[i].val=v
        nodes[i].parent=p
        nodes[p].children.append(nodes[i])
    solution=Solution()
    ans=solution.max_heap(nodes[0])
    print(ans)
