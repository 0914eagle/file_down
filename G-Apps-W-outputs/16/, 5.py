
import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def dfs(node, parent_val):
    beauty = gcd(node.val, parent_val)
    for child in node.children:
        beauty = max(beauty, dfs(child, beauty))
    return beauty

def solve_tree_beauty(n, a, edges):
    nodes = [TreeNode(val) for val in a]
    for x, y in edges:
        nodes[x-1].children.append(nodes[y-1])
    
    result = []
    for i in range(n):
        result.append(dfs(nodes[i], nodes[i].val))
    
    return result

# Reading input
n = int(input())
a = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

# Solving and printing output
result = solve_tree_beauty(n, a, edges)
print(*result)
