
# 两两颜色的集合
# C、M、Y 两两颜色的集合
# C+M、C+Y、M+C、M+Y、Y+C、Y+M
# 遍历列表，判断集合是否有交集
n = int(input())
s = input()
color = set(['C', 'M', 'Y'])
# 题意理解有误，当三个颜色的位置都相同时，无法满足条件
for i in range(1, n):
    if s[i] == s[i-1] and s[i] != '?':
        print('No')
        exit(0)
if s.count('?') % 2 == 1:
    print('Yes')
else:
    print('No')
