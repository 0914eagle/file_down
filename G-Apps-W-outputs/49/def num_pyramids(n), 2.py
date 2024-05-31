
def num_pyramids(n):
    pyramids = 0
    height = 1
    
    while n >= (height + 1) * (height + 2) // 2:
        n -= (height + 1) * (height + 2) // 2
        height += 1
        pyramids += 1
        
    return pyramids

t = int(input())
for _ in range(t):
    n = int(input())
    print(num_pyramids(n))
