
# 贪心
# 1. 先判断是否可以加
# 2. 加的位置
# 3. 加的数字
# 4. 加号的位置

s = input()

def check(s, i):
    a = int(s[:i])
    b = int(s[i:])
    return a + b == int(s)

for i in range(1, len(s)):
    if check(s, i):
        print(s[:i] + '+' + s[i:] + '=' + s)
        break
