
# http://codeforces.com/contest/1108/problem/A

n,k = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
for i in a:
    if i[0] < i[1]:
        print("YES")
        print(i[0],i[0],i[0],i[0])
    else:
        print("YES")
        print(i[1],i[1],i[1],i[1])

