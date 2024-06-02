
def construct_binary_string(n, s):
    w = ''
    for i in range(n):
        char = s[i]
        w += char
    return w

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    result = construct_binary_string(n, s)
    print(result)
