
# coding: utf-8

# In[ ]:


'''
解题思路：
只要令b1和q满足公式
    b1 + q * n = a
    b1 = a - q * n

'''

# coding: utf-8

# In[ ]:


'''
解题思路：
只要令b1和q满足公式
    b1 + q * n = a
    b1 = a - q * n

'''

b1, q, l, m = list(map(int, input().split()))
l = abs(l)
a = list(map(int, input().split()))

for i in range(m):
    a[i] = abs(a[i])

a.sort()

count = 0

for i in range(1, l + 1):
    if b1 + q * i < a[0]:
        count += 1
    elif b1 + q * i > a[0]:
        break

for i in range(m):
    if b1 == a[i]:
        break
    if b1 > a[i]:
        continue
    while b1 + q * i < a[i]:
        count += 1
    else:
        b1 = a[i] - q * i

print(count)

/Algorithms/1107.md
# 1107. 连通网络的操作
