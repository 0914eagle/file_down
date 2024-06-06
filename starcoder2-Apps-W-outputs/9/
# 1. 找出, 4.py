
# 1. 找出所有可能的k值，并计算出对应的rating
# 2. 去重
# 3. 排序

t = int(input())
for _ in range(t):
    n = int(input())
    res = set()
    for k in range(1, n+1):
        res.add(n//k)
    res = list(res)
    res.sort()
    print(len(res))
    print(*res)
