
def construct_string(n, k, t):
    prefix = ""
    for i in range(n):
        prefix += t[:i+1]
        if prefix.count(t) == k:
            break
    return prefix

n, k = map(int, input().split())
t = input().strip()

result = construct_string(n, k, t)
print(result)
