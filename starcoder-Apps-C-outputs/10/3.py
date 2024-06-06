
# 找到最高且最低的数字

# 第二遍输入的列表中有相同的数字

# 找出第二遍输入的列表中，找到和最高数字相同的数字所在的位置，获得这个数字在第一遍输入的列表中对应的位置

# 找到这个位置对应的第二个数

# 找到这个数所在的位置

# 输出这个数对应的第二个数


m,q=map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
b = [int(input()) for _ in range(q)]
a.sort(key=lambda x:x[2])
c = a[0][1]
d = a[-1][1]
for i in b:
    print(a[i-1][1],a[i-1][1])


