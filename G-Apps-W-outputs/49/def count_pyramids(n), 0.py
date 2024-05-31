
def count_pyramids(n):
    total_pyramids = 0
    height = 1

    while n >= height + (height + 1):
        total_pyramids += 1
        n -= height + (height + 1)
        height += 1

    return total_pyramids

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_pyramids(n))
