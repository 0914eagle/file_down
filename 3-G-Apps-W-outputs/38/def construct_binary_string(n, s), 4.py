
def construct_binary_string(n, s):
    w = ""
    for i in range(n):
        if s[i] == s[i + n - 1]:
            w += s[i]
        else:
            w += "0"
    return w

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    result = construct_binary_string(n, s)
    print(result)
