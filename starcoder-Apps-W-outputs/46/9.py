

# 解题思路：
# 这道题的思路是很简单的，就是先让给定的序列变成两个数组，然后比较两个数组的大小。
# 注意有些case的情况，比如[1,2,1,2]，这种情况就是第一个人获胜

import sys

def judge(x, y):
    if len(x) != len(y):
        return 0
    if len(x) == 0:
        return 1
    else:
        if x[0] == y[0]:
            return judge(x[1:], y[1:])
        else:
            return x[0] > y[0]
            

# 题目给定两个数组，分别代表两个选手的得分，题目要求输出哪个选手赢
n = int(sys.stdin.readline().strip())
a = []
b = []
for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        a.append(x)
    else:
        b.append(-x)

if judge(a, b):
    print('first')
elif judge(b, a):
    print('second')
else:
    print('first')

