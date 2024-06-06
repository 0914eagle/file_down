
a, b, l, r = map(int, input().split())

# 第一个人

def solve(x, y):
    # x, y 是当前字符串的长度，长度为 y 的字符串应该在前面拼接 y 个长度为 x 的字符串
    if x >= y:
        return (x - y) * y + y
    return solve(x + 1, y - x)

print(solve(a, b))
