
def solve(a):
    a.sort()
    min_dist = float('inf')
    
    for i in range(len(a) - 1):
        dist = a[i + 1] - a[i]
        
        if dist < min_dist:
            min_dist = dist
    
    return min_dist

N = int(input())
a = list(map(int, input().split()))

print(solve(a))

