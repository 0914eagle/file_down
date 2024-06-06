
#输入字符串
a = input()
b = input()
#将两个字符串的长度设为相等
if len(a) > len(b):
    a, b = b, a
#将字符转换为二进制数
x = int(a, 2)
y = int(b, 2)
#计算两个二进制数的异或和
z = x ^ y
#比较异或和和字符串的长度是否相等
if len(bin(z)) - 2 == len(a):
    print('YES')
else:
    print('NO')
