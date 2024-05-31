
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def calculate_beauty(vertex, parent, numbers, adj_list, gcd_so_far):
    current_gcd = gcd(gcd_so_far, numbers[vertex])
    beauty = max(numbers[vertex], current_gcd)
    for child in adj_list[vertex]:
        if child != parent:
            beauty = max(beauty, calculate_beauty(child, vertex, numbers, adj_list, current_gcd))
    return beauty

def max_beauty(n, numbers, edges):
    adj_list = [[] for _ in range(n)]
    for x, y in edges:
        adj_list[x-1].append(y-1)
        adj_list[y-1].append(x-1)
    
    result = []
    for i in range(n):
        result.append(calculate_beauty(i, -1, numbers, adj_list, 0))
    
    return result

# Input
n = int(input())
numbers = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

# Output
result = max_beauty(n, numbers, edges)
print(*result)
