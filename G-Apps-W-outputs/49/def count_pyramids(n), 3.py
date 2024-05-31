
def count_pyramids(n):
    count = 0
    height = 1
    while n >= height*(height+1)//2:
        n -= height*(height+1)//2
        height += 1
        count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_pyramids(n))
