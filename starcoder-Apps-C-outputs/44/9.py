
# 20200109230907
# https://codeforces.com/contest/1253/problem/E

# ans=min(4,t)
# ans=min(t//2,t-2)
# n=len(str(a_x))
# if n*ans<10**16:
#     print(ans)
# else:
#     print(0)

# a, b, c = 1, 2, 3
# print(a,b,c)
# print((a,b,c))
# print(type(a))
# print(type((a,b,c)))
# print(*[1, 2, 3])
# print(type(*[1, 2, 3]))

# (10,20,30)
# [10,20,30]

# print(1, 2, 3)

# for i in range(4):
#     print(i)
# print(*range(4))

x_0, y_0, a_x, a_y, b_x, b_y = map(int, input().split())
x_s, y_s, t = map(int, input().split())

x, y = x_s, y_s
ans = 0
for i in range(min(t+1, 4)):
    if x==x_0 and y==y_0:
        ans += 1
    x, y = a_x*x+b_x, a_y*y+b_y

print(ans)
