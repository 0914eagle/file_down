

n = int(input())
h = [0 for i in range(n)]
w = [0 for i in range(n)]
book = [0 for i in range(n)]
for i in range(n):
    s = input().split(" ")
    h[i] = int(s[0])
    w[i] = int(s[1])
min_area = pow(10, 8)
book[0] = 1
book[1] = 2
book[2] = 3
def dfs(n,index,depth,height,area):
    if index == n:
        if depth > 0 and height > 0 and area < min_area:
            min_area = area
        return
    for i in range(3):
        if book[i] == 0:
            book[i] = index + 1
            if i == 0:
                dfs(n,index+1,depth,max(height,h[index]),area)
            else:
                dfs(n,index+1,depth+w[index],max(height,h[index]),area+depth*height)
            book[i] = 0
dfs(n,3,0,0,0)
print(min_area)
