
# 读入
n, m = map(int, input().split())
# print(n, m)
a = list(map(int, input().split()))
# print(a)
b = list(map(int, input().split()))
# print(b)
a.sort()
b.sort(reverse = True)
# print(a)
# print(b)
print(a[1] * b[0])
