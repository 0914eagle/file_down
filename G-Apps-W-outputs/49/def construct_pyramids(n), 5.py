
def construct_pyramids(n):
    pyramids = 0
    height = 1

    while n >= height * (height + 1) // 2:
        n -= height * (height + 1) // 2
        pyramids += 1
        height += 1

    return pyramids

t = int(input())
for _ in range(t):
    n = int(input())
    print(construct_pyramids(n))
