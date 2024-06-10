
n,h = map(int, input().split())
a = list(map(int, input().split()))

min_width = 0
for elem in a:
    if elem > h:
        min_width += 2
    else:
        min_width += 1
        
print(min_width)

