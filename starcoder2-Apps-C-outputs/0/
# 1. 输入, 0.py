
# 1. 输入公司数量
C = int(input())
# 2. 循环输入公司的股票数量
for i in range(C):
    K = int(input())
    # 3. 定义一个字典，键是日期，值是股票数量
    d = {}
    # 4. 循环输入每天的股票数量
    for j in range(K):
        N, D = map(int, input().split())
        # 5. 字典中如果没有该日期，则添加该日期，并将股票数量赋值给该日期
        if D not in d:
            d[D] = N
        # 6. 如果字典中有该日期，则将该日期的股票数量加上输入的股票数量
        else:
            d[D] += N
    # 7. 循环输出字典中每天的股票数量
    for k in sorted(d):
        print(d[k], end=' ')
    print()
