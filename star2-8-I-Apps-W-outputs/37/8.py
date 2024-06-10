
n, h = map(int, input().split())
a = list(map(int, input().split()))

num_bent = 0
for height in a:
    if height > h:
        num_bent += 1

width = len(a) + num_bent
print(width)

